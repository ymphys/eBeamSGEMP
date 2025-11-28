# **Prompt：请生成完整可运行的 `gaussian_macro.py`（宏脉冲频谱计算）**

## **程序目标**

编写一个 Python 程序 `gaussian_macro.py`，用于计算和绘制由重复微脉冲构成的**宏脉冲电场频谱**。
宏脉冲持续时间：**1 微秒**
每个微脉冲持续时间远小于周期，微脉冲之间的间隔：
[
T = 550~\text{ps}
]

频域宏脉冲电场表达式：
[
\tilde{E}_x(\omega)
===================

\tilde{E}*{\text{pulse}-x}(\omega)
\cdot
\frac{\sin!\left((2k*{\max}+1)\omega T /2\right)}
{\sin!\left(\omega T /2\right)}
]

其中
[
k_{\max} = \mathrm{int}\left(\frac{1\ \mu s}{2T}\right)
]

微脉冲频域电场（给定解析形式）：
[
\tilde{E}_{\text{pulse}-x}(\omega)
==================================

-\frac{Ne\gamma}{4\pi\epsilon_0d^2}
\exp\left(-\frac{\omega^2\tau_0^2}{4}\right)
\left(
\frac{\sqrt{2}\omega t_0^2}{\sqrt{\pi}\beta^2\gamma^2}
K_1\left(\frac{\omega t_0}{\beta\gamma}\right)
\right)
]
其中 (K_1) 为第二类修正贝塞尔函数（scipy.special.k1）。

---

# **1. 程序功能要求**

`gaussian_macro.py` 必须完成：

1. **计算频率数组**

   * 使用指定频率范围，例如 0 到 **3 THz**（可根据时间特征确定）
   * 频率点数 `Nw`（建议 5000）

2. **生成角频率数组**
   [
   \omega = 2\pi f
   ]

3. **计算微脉冲频域电场 (\tilde{E}_{\text{pulse}-x})**
   使用给定解析式和 Bessel K1。

4. **计算干涉因子**
   [
   F(\omega)=\frac{\sin((2k_{\max}+1)\omega T/2)}{\sin(\omega T/2)}
   ]
   并处理分母为零的情况。

5. **计算宏脉冲频域电场**
   [
   \tilde{E}*x(\omega)=\tilde{E}*{\text{pulse}-x}(\omega)\cdot F(\omega)
   ]

6. **绘制并保存图像（中文标签）**

   * 图 1：微脉冲频域幅值
   * 图 2：宏脉冲频域幅值
   * 输出文件：`macro_spectrum.png`

---

# **2. 物理常数**

程序需定义：

```python
e = 1.6e-19
epsilon_0 = 8.85e-12
c = 3e8
```

---

# **3. 参数与默认值**

```python
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
```

---

# **4. 中文显示设置（必须）**

程序开头加入：

```python
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Heiti TC','STHeiti','SimHei','Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False
```

---

# **5. 必须定义的函数**

程序至少包含：

### **(1) compute_micro_spectrum(omega, params)**

根据解析公式计算 (\tilde{E}_{\text{pulse}-x}(\omega))

### **(2) compute_macro_spectrum(omega, E_micro, T, k_max)**

计算干涉因子 F(ω)，再算 E_macro(ω)

### **(3) plot_spectra(...)**

绘制微脉冲与宏脉冲频谱（2×1 布局）

---

# **6. 绘图要求（中文）**

图 1：微脉冲频谱

* 标题：“微脉冲频域电场幅值”
* 横轴：“频率 f（Hz）”
* 纵轴：“幅值 |E(ω)|”

图 2：宏脉冲频谱

* 标题：“宏脉冲电场频谱（1 微秒宏脉冲，T=550 ps）”

包含网格、中文字体、图例。

---

# **7. 输出文件**

运行后必须生成：

`macro_spectrum.png`

---

# **8. 主程序结构**

在 `if __name__ == "__main__":` 中：

1. 初始化参数
2. 生成频率数组
3. 计算微脉冲频谱
4. 计算宏脉冲频谱
5. 绘图保存

---

# **请按以上所有要求生成完整、可运行的 `gaussian_macro.py` 源代码。**