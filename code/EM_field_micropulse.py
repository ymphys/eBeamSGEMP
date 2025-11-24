"""
Electromagnetic field of a finite-length relativistic electron beam pulse.

Model summary:
    - Electrons travel along +z with speed v0 (beta = v0 / c).
    - The uniform line-charge density inside the co-moving window is
      lambda = e * N / (2 * v0 * tau0) for z' in [-v0 * tau0, v0 * tau0].
    - The observation point sits at (d, 0, 0).
    - Total fields are obtained by integrating the single-charge contribution
      over the beam slice.

Outputs:
    1. Time traces for |E|(t), (E_x, E_z)(t), |B|(t), and B_y(t) over [-2 * tau0, 2 * tau0].
    2. Visualization arranged in four stacked subplots for quick comparison.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

import matplotlib
# 设置中文字体和负号显示（如有需要）
matplotlib.rcParams['font.sans-serif'] = ['Heiti TC', 'STHeiti', 'SimHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False  # Use ASCII minus

# =============================================================================
# CONSTANTS
# =============================================================================
E_CHARGE = 1.602e-19      # Coulomb
EPSILON_0 = 8.854e-12     # F/m
C = 3.0e8                 # m/s
ME_C2_MEV = 0.511         # Electron rest energy in MeV


# =============================================================================
# RELATIVISTIC AND BEAM PARAMETERS
# =============================================================================
def relativistic_parameters(Ek_MeV: float) -> tuple[float, float, float]:
    """Return gamma, beta, and v0 for a beam with kinetic energy Ek (MeV)."""
    gamma = 1.0 + Ek_MeV / ME_C2_MEV
    beta = np.sqrt(1.0 - 1.0 / (gamma * gamma))
    v0 = beta * C
    return gamma, beta, v0


def uniform_line_charge_density(N: float, v0: float, tau0: float) -> float:
    """lambda = e * N / (2 * v0 * tau0)."""
    return E_CHARGE * N / (2.0 * v0 * tau0)


# =============================================================================
# FIELD INTEGRALS
# =============================================================================
def _component_integral(
    t: float,
    component_fn,
    beta: float,
    v0: float,
    lam: float,
    d: float,
    z_min: float,
    z_max: float,
) -> float:
    """Integrate one Cartesian component at time t over the beam slice."""
    prefactor = -lam / (4.0 * np.pi * EPSILON_0) * (1.0 - beta * beta)

    def integrand(zp: float) -> float:
        rz = zp + v0 * t
        r2 = d * d + rz * rz
        geom_factor = component_fn(rz)
        denom = (1.0 - beta * beta * d * d / r2) ** 1.5
        return prefactor * geom_factor / (denom * (r2 ** 1.5))

    value, _ = quad(integrand, z_min, z_max, limit=400)
    return value


def compute_pulse_fields(
    times: np.ndarray,
    beta: float,
    v0: float,
    lam: float,
    d: float,
    tau0: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Evaluate E_x(t), E_z(t), and B_y(t) on the provided timeline."""
    z_min = -v0 * tau0
    z_max = v0 * tau0

    e_x = np.zeros_like(times)
    e_z = np.zeros_like(times)

    comp_x = lambda _: d
    comp_z = lambda rz: rz

    for idx, t in enumerate(times):
        e_x[idx] = _component_integral(t, comp_x, beta, v0, lam, d, z_min, z_max)
        e_z[idx] = _component_integral(t, comp_z, beta, v0, lam, d, z_min, z_max)

    b_y = (v0 / (C * C)) * e_x
    return e_x, e_z, b_y


# =============================================================================
# VISUALIZATION
# =============================================================================
def plot_fields(times, e_x, e_z, b_y) -> None:
    """Plot |E|, (E_x, E_z), |B|, and B_y on four stacked subplots."""
    e_mag = np.sqrt(e_x**2 + e_z**2)
    b_mag = np.abs(b_y)

    fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=True)
    ax_flat = axes.flatten()

    ax_flat[0].plot(times*1e9, e_mag, color="tab:purple")
    ax_flat[0].set_ylabel("电场幅值 (V/m)")
    ax_flat[0].set_title("电场脉冲", fontsize=11)
    ax_flat[0].grid(True, linestyle="--", alpha=0.4)

    ax_flat[1].plot(times, e_x, label="E_x", color="tab:blue")
    ax_flat[1].plot(times, e_z, label="E_z", color="tab:orange")
    ax_flat[1].set_ylabel("电场分量 (V/m)")
    ax_flat[1].set_title("电场分量", fontsize=11)
    ax_flat[1].legend(loc="upper right")
    ax_flat[1].grid(True, linestyle="--", alpha=0.4)

    ax_flat[2].plot(times, b_mag, color="tab:green")
    ax_flat[2].set_ylabel("磁场幅值 (T)")
    ax_flat[2].set_title("磁场幅值", fontsize=11)
    ax_flat[2].grid(True, linestyle="--", alpha=0.4)
    ax_flat[2].set_xlabel("Time (s)")

    ax_flat[3].plot(times, b_y, color="tab:red")
    ax_flat[3].set_ylabel("磁场分量 (T)")
    ax_flat[3].set_title("磁场分量", fontsize=11)
    ax_flat[3].set_xlabel("Time (s)")
    ax_flat[3].grid(True, linestyle="--", alpha=0.4)

    fig.suptitle("一维均匀分布的电子束微脉冲产生的电磁脉冲", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    plt.show()


# =============================================================================
# MAIN ROUTINE
# =============================================================================
def main():
    # Beam / geometry parameters from the prompt
    d = 1.0          # m
    Ek = 10.0        # MeV
    N = 1e10         # electrons
    tau0 = 1e-10     # s

    _, beta, v0 = relativistic_parameters(Ek)
    lam = uniform_line_charge_density(N, v0, tau0)

    times = np.linspace(-100 * tau0, 100 * tau0, 20000)
    e_x, e_z, b_y = compute_pulse_fields(times, beta, v0, lam, d, tau0)

    print(
        f"beta = {beta:.6f}, v0 = {v0:.3e} m/s, line charge density lambda = {lam:.3e} C/m"
    )
    plot_fields(times, e_x, e_z, b_y)


if __name__ == "__main__":
    main()
