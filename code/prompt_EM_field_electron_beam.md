# Prompt：生成 `gaussian_micro.py` 的详细说明

## 概述（Overview）

请编写一个单文件 Python 程序 `gaussian_micro.py`，功能如下：

1. 数值计算下列时变电磁场（随时间 (t) 变化）：
   [
   \begin{aligned}
   E_{\text{pulse}-x}(t)
   &=-\frac{Ne\gamma}{4\pi\epsilon_0d^2}\frac{1}{\operatorname{Erf}(2)\sqrt{\pi}\tau_0}\int_{-2\tau_0}^{2\tau_0} d\tau\ \exp\left(-\frac{\tau^2}{\tau_0^2}\right)\frac{1}{\left[1+\beta^2\gamma^2(\tau+t)^2/t_0^2\right]^{3/2}}\
   E_{\text{pulse}-z}(t)
   &=-\frac{Ne}{4\pi\epsilon_0d^2}\frac{\beta\gamma}{\operatorname{Erf}(2)\sqrt{\pi}\tau_0t_0}\int_{-2\tau_0}^{2\tau_0} d\tau\ \exp\left(-\frac{\tau^2}{\tau_0^2}\right)\frac{\tau+t}{\left[1+\beta^2\gamma^2(\tau+t)^2/t_0^2\right]^{3/2}}\
   B_{\text{pulse}-y}(t)&=\frac{\beta}{c}E_{\text{pulse}-x}(t)
   \end{aligned}
   ]
   其中 (\operatorname{Erf}(2)\approx0.995)。

2. 参数、默认值、常数和时间采样如下（必须使用这些默认值，且在代码中清晰注释）：

* 常数：
  `e = 1.6e-19`（库仑）， `epsilon_0 = 8.85e-12`（F/m）， `c = 3e8`（m/s）。
* 参数与默认值：
  `Ek = 10e6*1.0`（10 MeV, 单位电子伏转换已在下文说明），使用 `gamma = 1 + Ek/0.511e6`（注意能量单位换算为 MeV），
  `beta = np.sqrt(1 - 1/gamma**2)`，
  `tau_0 = 100e-12`（秒）， `d = 1.0`（米）， `t_0 = d / c`（秒），
  `N` 的取值请设为 `N = 1e9`（默认，可以在脚本顶部作为可改参数）。
* 时间 `t` 取值范围：从 `-1e-9` 到 `1e-9`（秒）。建议时间点数 `Nt = 2001`（或同等密度），并在代码顶部易于修改。
* 积分变量 (\tau) 的积分区间严格为 ([-2\tau_0,,2\tau_0])。用于数值积分的 (\tau) 采样点建议 `Ntau = 2001`（或足够多以确保精度）。

3. 数值方法要求（明确具体实现方法）：

* 使用 NumPy 向量化操作进行积分，优先使用复合 Simpson 或复合梯形积分（`scipy.integrate.simpson` 或 `numpy.trapz`）。若使用 `scipy.integrate.quad` 为单根函数在每个 t 上调用会很慢，除非做自适应并行；推荐**对全部 t 向量化**并对 (\tau) 使用 `simpson`/`trapz`。
* 对 (E_x(t)) 和 (E_z(t)) 的积分，构造一个形状为 `(Nt, Ntau)` 的数组时需要注意内存（若内存过大，可说明如何用逐 t 循环但仍使用高精度积分）。提示：`tau` 与 `t` 可以通过广播生成 `(Nt, Ntau)` 的 `tau_plus_t = tau[np.newaxis,:] + t[:,np.newaxis]`，然后计算被积函数并对 `axis=1` 积分得到每个 t 的值。
* 在实现中写明误差函数 `Erf(2)` 的获取方法：使用 `scipy.special.erf(2)` 或直接写常数 `0.995`（更推荐用 `scipy.special.erf` 以保证严谨）。

4. 可视化要求（必须严格按下列要求绘图）：

* 使用 `matplotlib`，并在脚本开头加入（用户提供的）中文字体设置：

```python
import matplotlib
# 设置中文字体和负号显示（如有需要）
matplotlib.rcParams['font.sans-serif'] = ['Heiti TC', 'STHeiti', 'SimHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False  # Use ASCII minus
```

* 绘图布局：`2x2` 子图（`plt.subplots(2,2, figsize=(12,9))` 等）：

  * 左上（`ax[0,0]`）：**电场幅值随时间**（绘制 ( |E_{\text{total}}(t)| ) 或 `np.sqrt(E_x**2 + E_z**2)`），纵轴与横轴均使用中文标签，图题用中文：例如“电场幅值随时间变化”。
  * 左下（`ax[1,0]`）：**磁场幅值随时间**（绘制 `|B_y(t)|` 或 `np.abs(B_y)`），中文标签与标题：“磁场幅值随时间变化”。
  * 右上（`ax[0,1]`）：**电场分量随时间变化**，用不同颜色和图例绘制 `E_x(t)` 与 `E_z(t)`（例如蓝/红），图例中文：`E_x` 与 `E_z`，标题“电场分量随时间变化”。
  * 右下（`ax[1,1]`）：**磁场分量随时间变化**，这里只有 `B_y`（仍用中文标题“磁场分量随时间变化”）。如果想显示 `B_y` 的正负，可用一条曲线并标注。
* 所有子图应包含网格、中文坐标刻度标签、中文单位（例如横轴 `t（s）`，纵轴示例 `电场强度（V/m）`、`磁场强度（T）`）。
* 添加一个总标题（中文），并在图的右上角或图内添加注释说明使用的主要参数（如 `Ek`、`tau_0`、`d`、`N`）。
* 设置合理的 y 轴刻度范围或使用对数刻度（可作为可选项，但需在代码中注释并提供切换方法）。

5. 文件/代码格式和运行细节（必须满足）：

* 程序文件名：**`gaussian_micro.py`**（首行注释写明用途）。
* 须包含 `if __name__ == "__main__":`，在其中设置默认参数并调用计算与绘图函数。
* 编写至少两个函数：

  * `compute_fields(t_array, params)`：返回 `E_x(t), E_z(t), B_y(t)`（NumPy 数组）。
  * `plot_fields(t_array, E_x, E_z, B_y, params)`：负责绘图与保存（例如 `gaussian_micro.png`）。
* 在文件顶部列出依赖项（`numpy`, `scipy`, `matplotlib`）并给出安装提示（例如 `pip install numpy scipy matplotlib`）。
* 在代码中添加充分的注释，解释每一步的物理含义和数值实现细节（积分方法、步长选择等）。
* 代码应对可能的数值问题进行合理防护（例如避免除以零、处理极端值、对大型数组的内存警告）。

6. 输出与可选增强功能（推荐但非必须）：

* 将绘图保存为 `gaussian_micro.png`（高分辨率 `dpi=300`），并在脚本中展示（`plt.show()`）。
* 在终端打印主要参数与运行耗时（使用 `time` 模块）。
* 提供命令行参数解析（可选，使用 `argparse`），允许用户修改 `N`, `Ek`, `tau_0`, `Nt` 等参数。

## 精确实现细节（逐步指令）

1. 在脚本头部写明文件名、功能与作者/日期注释。
2. 导入包：

```python
import time
import numpy as np
from scipy import special
from scipy.integrate import simpson  # 或使用 numpy.trapz
import matplotlib
import matplotlib.pyplot as plt
```

3. 设置中文显示（如上）。
4. 定义物理常数与默认参数（注释单位）：

```python
e = 1.6e-19
epsilon_0 = 8.85e-12
c = 3e8

# 参数（默认）
N = 1e9
Ek_MeV = 10.0  # MeV
gamma = 1.0 + Ek_MeV / 0.511  # 0.511 MeV 是静止电子质量能量
beta = np.sqrt(1.0 - 1.0/gamma**2)
tau_0 = 100e-12
d = 1.0
t_0 = d / c
```

5. 在 `compute_fields` 中：

* 生成 `t_array = np.linspace(-1e-9, 1e-9, Nt)`。
* 生成 `tau_array = np.linspace(-2*tau_0, 2*tau_0, Ntau)`。
* 使用广播构造 `tau_plus_t = tau_array[np.newaxis, :] + t_array[:, np.newaxis]`（注意形状： `(Nt, Ntau)` 或相反，根据实现）。
* 计算指数因子 `exp(-tau^2 / tau_0**2)`（为 `(Ntau,)`，可广播）。
* 计算分母 `den = (1 + beta**2 * gamma**2 * (tau_plus_t)**2 / t_0**2)**(3/2)`，然后构造被积函数 `f_x = exp_factor * 1.0 / den`； `f_z = exp_factor * (tau_plus_t) / (t_0 * den)`（注意 `t_0` 的位置与量纲）。
* 对 `tau` 方向积分：`E_x_prefactor = -N * e * gamma / (4*np.pi*epsilon_0 * d**2) / (special.erf(2)*np.sqrt(np.pi)*tau_0)`，然后 `E_x = E_x_prefactor * simpson(f_x, tau_array, axis=1)`（或 `trapz`）。
* 类似地计算 `E_z` 并把 `B_y = beta/c * E_x`。
* 返回数组 `E_x, E_z, B_y` 对应 `t_array`。
* 在代码注释中解释每个常数、每个乘子。

6. 在绘图函数中：

* 使用 `fig, axs = plt.subplots(2,2, figsize=(12,9))`。
* 左上绘 `np.sqrt(E_x**2 + E_z**2)`，横轴 `t (s)` 的中文写法：`'时间 t（s）'`，纵轴 `电场幅值（V/m）`。
* 左下绘 `np.abs(B_y)`, 纵轴 `磁场幅值（T）`。
* 右上绘 `E_x` 与 `E_z` 两条曲线，添加中文图例 `['E_x', 'E_z']` 与网格。
* 右下绘 `B_y`（可以同时绘 `B_y` 的绝对值和原始值）。
* 设置中文标题与总标题（例如 `fig.suptitle('时变电磁场脉冲（高斯谱）', fontsize=16)`）。
* 保存 `plt.savefig('gaussian_micro.png', dpi=300, bbox_inches='tight')`，并 `plt.show()`。

7. 在 `__main__` 中：

* 解析可选命令行参数（建议但可选）。
* 打印参数和开始时间，调用 `compute_fields`，打印运行时间并保存/显示图像。

## 代码示例片段（展示如何调用数值积分；仅示例，请在最终文件中写成完整、可运行代码）

```python
# 注意：这是片段示例，最终请提交完整可执行文件 gaussian_micro.py
tau = np.linspace(-2*tau_0, 2*tau_0, Ntau)
t = np.linspace(-1e-9, 1e-9, Nt)
# broadcasting
T, TAU = np.meshgrid(t, tau, indexing='ij')  # T shape (Nt, Ntau)
tau_plus_t = TAU + T
exp_factor = np.exp(-TAU**2 / tau_0**2)  # shape (Nt, Ntau)
den = (1 + beta**2 * gamma**2 * (tau_plus_t)**2 / t_0**2)**(1.5)
f_x = exp_factor / den
# integrate over tau (axis=1)
E_x = E_x_prefactor * simpson(f_x, tau, axis=1)
```

## 验证、数值稳定性与故障排除（Troubleshooting）

* 如果运行很慢或内存不足：

  * 降低 `Nt` 或 `Ntau`（例如 `Nt=1001, Ntau=1001`），或改用对每个 t 单独循环但在 t 循环中使用 `simpson`（如果内存受限，单点循环比广播更省内存）。
  * 使用 `numpy.trapz` 比 `simpson` 更节省计算（但精度可能稍低）。
* 如出现除零或溢出，添加小的正则化项，例如 `den = np.maximum(den, 1e-30)` 或 `tau_plus_t = np.where(np.isfinite(tau_plus_t), tau_plus_t, 0.0)`。
* 若中文字体不显示，尝试安装系统字体或将 `matplotlib.rcParams['font.sans-serif']` 中的项改为本机可用字体（在代码注释中说明）。
* 若 `scipy` 不可用，说明如何用 `numpy.trapz` 替代 `simpson`。

## 交付要求（Deliverables）

* 单个文件 `gaussian_micro.py`（完整、可直接运行并生成一个 PNG 图），文件头注明依赖与运行方法（示例：`python gaussian_micro.py`）。
* 文件内部必须包含 `compute_fields` 与 `plot_fields` 两个函数及必要注释。
* 在文件中明确记录默认参数（可改动）与输出文件名 `gaussian_micro.png`。
