import numpy as np
import matplotlib.pyplot as plt
from scipy.special import k1
import matplotlib

# 设置中文字体和负号显示（如有需要）
matplotlib.rcParams['font.sans-serif'] = ['Heiti TC', 'STHeiti', 'SimHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False  # Use ASCII minus

# 物理常数
e = 1.6e-19
epsilon_0 = 8.85e-12
c = 3e8

# 参数与默认值
N = 1e9        # 电子数
Ek = 10e6      # 10 MeV
gamma = 1 + Ek / 0.511e6
beta = np.sqrt(1 - 1/gamma**2)
tau_0 = 100e-12
d = 1.0
t_0 = d / c
T = 550e-12
macro_duration = 1e-6
k_max = int(macro_duration / (2*T))

def compute_micro_spectrum(omega, params):
    """
    计算微脉冲频域电场 E_pulse_x(omega)
    
    参数:
    omega: 角频率数组
    params: 参数字典，包含 N, e, gamma, epsilon_0, d, tau_0, t_0, beta
    
    返回:
    E_micro: 微脉冲频域电场数组
    """
    N_val = params['N']
    e_val = params['e']
    gamma_val = params['gamma']
    epsilon_0_val = params['epsilon_0']
    d_val = params['d']
    tau_0_val = params['tau_0']
    t_0_val = params['t_0']
    beta_val = params['beta']
    
    # 计算微脉冲频域电场
    prefactor = -N_val * e_val * gamma_val / (4 * np.pi * epsilon_0_val * d_val**2)
    gaussian_term = np.exp(-omega**2 * tau_0_val**2 / 4)
    bessel_term = (np.sqrt(2) * omega * t_0_val**2) / (np.sqrt(np.pi) * beta_val**2 * gamma_val**2)
    bessel_k1 = k1(omega * t_0_val / (beta_val * gamma_val))
    
    E_micro = prefactor * gaussian_term * bessel_term * bessel_k1
    return E_micro

def compute_macro_spectrum(omega, E_micro, T, k_max):
    """
    计算宏脉冲频域电场 E_x(omega)
    
    参数:
    omega: 角频率数组
    E_micro: 微脉冲频域电场
    T: 微脉冲间隔
    k_max: 最大k值
    
    返回:
    E_macro: 宏脉冲频域电场数组
    F: 干涉因子数组
    """
    # 计算干涉因子 F(omega)
    numerator = np.sin((2 * k_max + 1) * omega * T / 2)
    denominator = np.sin(omega * T / 2)
    
    # 处理分母为零的情况
    F = np.zeros_like(omega)
    mask = np.abs(denominator) > 1e-12  # 避免除零
    F[mask] = numerator[mask] / denominator[mask]
    
    # 在分母接近零时使用极限值
    zero_mask = ~mask
    F[zero_mask] = (2 * k_max + 1) * np.cos((2 * k_max + 1) * omega[zero_mask] * T / 2)
    
    E_macro = E_micro * F
    return E_macro, F

def plot_spectra(f, E_micro, E_macro, output_file='macro_spectrum.png'):
    """
    绘制微脉冲和宏脉冲频谱
    
    参数:
    f: 频率数组 (Hz)
    E_micro: 微脉冲频域电场
    E_macro: 宏脉冲频域电场
    output_file: 输出文件名
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # 图1: 微脉冲频谱
    ax1.plot(f, np.abs(E_micro), 'b-', linewidth=1.5, label='微脉冲频谱')
    ax1.set_xlabel('频率 f (Hz)')
    ax1.set_ylabel('幅值 |E(ω)|')
    ax1.set_title('微脉冲频域电场幅值')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    
    # 图2: 宏脉冲频谱
    ax2.plot(f, np.abs(E_macro), 'r-', linewidth=1.5, label='宏脉冲频谱')
    ax2.set_xlabel('频率 f (Hz)')
    ax2.set_ylabel('幅值 |E(ω)|')
    ax2.set_title('宏脉冲电场频谱（1 微秒宏脉冲，T=550 ps）')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # 1. 初始化参数
    params = {
        'N': N,
        'e': e,
        'gamma': gamma,
        'epsilon_0': epsilon_0,
        'd': d,
        'tau_0': tau_0,
        't_0': t_0,
        'beta': beta
    }
    
    print(f"参数设置:")
    print(f"电子数 N = {N:.2e}")
    print(f"能量 Ek = {Ek/1e6:.1f} MeV")
    print(f"洛伦兹因子 gamma = {gamma:.6f}")
    print(f"速度比 beta = {beta:.6f}")
    print(f"微脉冲间隔 T = {T:.2e} s")
    print(f"宏脉冲持续时间 = {macro_duration:.2e} s")
    print(f"k_max = {k_max}")
    
    # 2. 生成频率数组
    f_max = 3e12  # 3 THz
    Nw = 5000
    f = np.linspace(1e6, f_max, Nw)  # 从1MHz开始避免零频率问题
    omega = 2 * np.pi * f
    
    print(f"\n频率范围: {f[0]/1e9:.2f} GHz 到 {f[-1]/1e12:.2f} THz")
    print(f"频率点数: {Nw}")
    
    # 3. 计算微脉冲频谱
    E_micro = compute_micro_spectrum(omega, params)
    print("微脉冲频谱计算完成")
    
    # 4. 计算宏脉冲频谱
    E_macro, F = compute_macro_spectrum(omega, E_micro, T, k_max)
    print("宏脉冲频谱计算完成")
    
    # 5. 绘图保存
    plot_spectra(f, E_micro, E_macro, 'macro_spectrum.png')
    print("图像已保存为 macro_spectrum.png")