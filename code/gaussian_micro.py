#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gaussian_micro.py

单文件脚本，用于根据高斯时间结构的电子微束计算时变电磁场并绘制 2x2 中文图。
依赖: numpy, scipy, matplotlib (pip install numpy scipy matplotlib)
运行: python gaussian_micro.py
"""

from __future__ import annotations

import argparse
import time
from dataclasses import dataclass

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from scipy.integrate import simpson

# 设置中文字体与负号显示
matplotlib.rcParams["font.sans-serif"] = [
    "Heiti TC",
    "STHeiti",
    "SimHei",
    "Arial Unicode MS",
]
matplotlib.rcParams["axes.unicode_minus"] = False

# -------------------------- 物理常数 (SI) --------------------------
E_CHARGE = 1.6e-19       # 电子电荷量 Coulomb
EPSILON_0 = 8.85e-12     # 真空介电常数 Farad/m
C_LIGHT = 3.0e8          # 光速 m/s
ERF_2 = special.erf(2.0)  # 精确调用误差函数，≈0.995322


@dataclass
class SimulationParams:
    """存放主要可调参数以及派生量，便于传递。"""

    N: float = 1e10              # 电子数量
    Ek_MeV: float = 10.0           # 束流动能 (MeV)
    tau_0: float = 100e-12         # 脉冲宽度 (s)
    distance: float = 1.0          # 探测点到束流轴距离 d (m)
    Nt: int = 2001                 # 时间采样点数
    Ntau: int = 2001               # tau 积分采样点数
    t_min: float = -1e-9           # 时间范围下限 (s)
    t_max: float = 1e-9            # 时间范围上限 (s)

    def __post_init__(self) -> None:
        # 电子静止能为 0.511 MeV
        self.gamma = 1.0 + self.Ek_MeV / 0.511
        self.beta = np.sqrt(max(0.0, 1.0 - 1.0 / self.gamma**2))
        self.t_0 = self.distance / C_LIGHT


def compute_fields(t_array: np.ndarray, params: SimulationParams) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    根据给定时间数组与参数计算 E_x, E_z, B_y。

    数值积分形式:
        E_x(t) ~ ∫ exp(-tau^2/tau_0^2) / [1 + beta^2 gamma^2 (tau+t)^2 / t_0^2]^{3/2} d tau
        E_z(t) ~ ∫ exp(-tau^2/tau_0^2) (tau+t) / [ ... ]^{3/2} d tau
        B_y(t) = (beta/c) * E_x(t)

    积分采用向量化 Simpson 复合求积，高斯权重由指数给出。
    """
    tau_array = np.linspace(-2.0 * params.tau_0, 2.0 * params.tau_0, params.Ntau)
    if params.Nt * params.Ntau > 5_000_000:
        print(
            "[提示] Nt 与 Ntau 的乘积较大，广播矩阵将占用约 "
            f"{params.Nt * params.Ntau * 8 / (1024**2):.1f} MB 内存。",
        )

    # 广播构造 (Nt, Ntau) 网格
    tau_plus_t = t_array[:, None] + tau_array[None, :]
    exp_factor = np.exp(-(tau_array / params.tau_0) ** 2)  # 仅依赖 tau

    denom = (
        1.0
        + (params.beta**2)
        * (params.gamma**2)
        * (tau_plus_t**2)
        / (params.t_0**2)
    ) ** 1.5
    denom = np.maximum(denom, 1e-30)  # 防止除零

    f_x = exp_factor[None, :] / denom
    f_z = exp_factor[None, :] * (tau_plus_t / params.t_0) / denom

    prefactor_ex = (
        -params.N
        * E_CHARGE
        * params.gamma
        / (4.0 * np.pi * EPSILON_0 * params.distance**2)
        / (ERF_2 * np.sqrt(np.pi) * params.tau_0)
    )
    prefactor_ez = (
        -params.N
        * E_CHARGE
        * params.beta
        * params.gamma
        / (4.0 * np.pi * EPSILON_0 * params.distance**2)
        / (ERF_2 * np.sqrt(np.pi) * params.tau_0)
    )

    E_x = prefactor_ex * simpson(f_x, tau_array, axis=1)
    E_z = prefactor_ez * simpson(f_z, tau_array, axis=1)
    B_y = params.beta / C_LIGHT * E_x

    return E_x, E_z, B_y


def compute_field_metrics(t_array: np.ndarray, E_x: np.ndarray, E_z: np.ndarray) -> dict[str, float]:
    """
    计算总电场（矢量和）的峰值与 FWHM，方便终端打印。
    若脉冲没有降到一半幅度，则返回 NaN。
    """
    field_mag = np.sqrt(E_x**2 + E_z**2)
    peak_idx = int(np.argmax(field_mag))
    E_peak = float(field_mag[peak_idx])
    t_peak = float(t_array[peak_idx])
    half_level = 0.5 * E_peak

    def _interpolate_cross(idx_low: int, idx_high: int) -> float:
        """在给定的两个点之间对半高位置做线性插值。"""
        y0, y1 = field_mag[idx_low], field_mag[idx_high]
        t0, t1 = t_array[idx_low], t_array[idx_high]
        if np.isclose(y0, y1):
            return float(t0)
        slope = (y1 - y0)
        return float(t0 + (half_level - y0) * (t1 - t0) / slope)

    left_time = np.nan
    for idx in range(peak_idx, -1, -1):
        if field_mag[idx] < half_level and idx + 1 < len(field_mag):
            left_time = _interpolate_cross(idx, idx + 1)
            break

    right_time = np.nan
    for idx in range(peak_idx, len(field_mag)):
        if field_mag[idx] < half_level and idx > 0:
            right_time = _interpolate_cross(idx - 1, idx)
            break

    fwhm = right_time - left_time if np.isfinite(left_time) and np.isfinite(right_time) else np.nan

    return {
        "E_peak": E_peak,
        "t_peak": t_peak,
        "FWHM": fwhm,
    }


def plot_fields(
    t_array: np.ndarray,
    E_x: np.ndarray,
    E_z: np.ndarray,
    B_y: np.ndarray,
    params: SimulationParams,
    outfile: str = "gaussian_micro.png",
) -> None:
    """绘制电磁场幅值与分量，并保存 PNG。"""
    field_magnitude = np.sqrt(E_x**2 + E_z**2)
    magnetic_magnitude = np.abs(B_y)

    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    ax = axes

    # 左上: 总电场
    ax[0, 0].plot(t_array, field_magnitude)
    ax[0, 0].set_title("电场幅值随时间变化")
    ax[0, 0].set_xlabel("时间 t（s）")
    ax[0, 0].set_ylabel("电场强度（V/m）")
    ax[0, 0].grid(True, linestyle="--", alpha=0.5)

    # 左下: 磁场幅值
    ax[1, 0].plot(t_array, magnetic_magnitude, color="green")
    ax[1, 0].set_title("磁场幅值随时间变化")
    ax[1, 0].set_xlabel("时间 t（s）")
    ax[1, 0].set_ylabel("磁场强度（T）")
    ax[1, 0].grid(True, linestyle="--", alpha=0.5)
    # 若需对数坐标，可启用下行代码：ax[1, 0].set_yscale("log")

    # 右上: 电场分量
    ax[0, 1].plot(t_array, E_x, label="E_x", color="tab:blue")
    ax[0, 1].plot(t_array, E_z, label="E_z", color="tab:red", linestyle="--")
    ax[0, 1].set_title("电场分量随时间变化")
    ax[0, 1].set_xlabel("时间 t（s）")
    ax[0, 1].set_ylabel("电场强度（V/m）")
    ax[0, 1].legend()
    ax[0, 1].grid(True, linestyle="--", alpha=0.5)

    # 右下: 磁场分量
    ax[1, 1].plot(t_array, B_y, color="purple")
    ax[1, 1].set_title("磁场分量随时间变化")
    ax[1, 1].set_xlabel("时间 t（s）")
    ax[1, 1].set_ylabel("磁场强度（T）")
    ax[1, 1].grid(True, linestyle="--", alpha=0.5)

    fig.suptitle("高斯微束时变电磁场模拟", fontsize=16)
    annotation = (
        f"N = {params.N:.2e}\n"
        f"Ek = {params.Ek_MeV:.2f} MeV\n"
        f"tau_0 = {params.tau_0*1e12:.1f} ps\n"
        f"d = {params.distance:.2f} m"
    )
    ax[0, 0].text(
        0.98,
        0.95,
        annotation,
        transform=ax[0, 0].transAxes,
        ha="right",
        va="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.7),
    )

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig(outfile, dpi=300, bbox_inches="tight")
    print(f"[信息] 图像已保存至 {outfile}")
    plt.show()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gaussian micro-pulse EM field calculator.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--N", type=float, default=1e10, help="电子数量")
    parser.add_argument("--Ek", type=float, default=10.0, help="束流动能 (MeV)")
    parser.add_argument("--tau0", type=float, default=100e-12, help="脉冲宽度 tau_0 (s)")
    parser.add_argument("--d", type=float, default=1.0, help="观测距离 d (m)")
    parser.add_argument("--Nt", type=int, default=2001, help="时间采样点数")
    parser.add_argument("--Ntau", type=int, default=2001, help="tau 积分采样点数")
    parser.add_argument("--tmin", type=float, default=-1e-9, help="时间范围下限 (s)")
    parser.add_argument("--tmax", type=float, default=1e-9, help="时间范围上限 (s)")
    parser.add_argument("--outfile", type=str, default="gaussian_micro.png", help="输出 PNG 名称")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    params = SimulationParams(
        N=args.N,
        Ek_MeV=args.Ek,
        tau_0=args.tau0,
        distance=args.d,
        Nt=args.Nt,
        Ntau=args.Ntau,
        t_min=args.tmin,
        t_max=args.tmax,
    )

    print("[信息] 关键参数设定：")
    print(
        f"    N = {params.N:.3e}, Ek = {params.Ek_MeV:.3f} MeV, "
        f"tau_0 = {params.tau_0:.3e} s, d = {params.distance:.2f} m"
    )
    print(
        f"    gamma = {params.gamma:.6f}, beta = {params.beta:.6f}, "
        f"Nt = {params.Nt}, Ntau = {params.Ntau}"
    )

    t_array = np.linspace(params.t_min, params.t_max, params.Nt)

    start = time.perf_counter()
    E_x, E_z, B_y = compute_fields(t_array, params)
    elapsed = time.perf_counter() - start
    print(f"[信息] 计算完成，耗时 {elapsed:.2f} s")

    metrics = compute_field_metrics(t_array, E_x, E_z)
    print(
        "[信息] 电场峰值/半高宽: "
        f"E_peak = {metrics['E_peak']:.3e} V/m, "
        f"t_peak = {metrics['t_peak']*1e12:.3f} ps, "
        f"FWHM = {metrics['FWHM']*1e12:.3f} ps"
    )

    plot_fields(t_array, E_x, E_z, B_y, params, outfile=args.outfile)


if __name__ == "__main__":
    main()
