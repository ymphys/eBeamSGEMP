## 匀速运动的单电子产生的电磁场

### 静止系

在该电子的静止系中，其电磁场为
$$
\vec{E}=-\frac{e}{4\pi\epsilon_0r^2}\hat{r},\quad\vec{B}=0.
$$
该电磁场的特点是各向同性，且不随时间变化。

如果距该电子1m处有一个电场探头，且其与电子保持相对静止，则其测到的场强应该为1.44nV/m. 

如果是一个包含$10^{10}$个电子的束团，且空间分布可忽略，则场强变为14.4V/m；如果探头距离进一步变为10cm，则场强变为1.44kV/m.

### 实验室系

如果电子在实验室系下以速度$\vec{v}=v\hat{z}$匀速运动，$t=0$时刻位于$(0,0,0)$位置，且电磁场探针固定在$(d,0,0)$处，则探针能测到的电磁场是随时间变化的
$$
\vec{E}(t)=-\frac{e}{4\pi\epsilon_0}\frac{1-\beta^2}{(1-\beta^2\sin^2\theta)^{3/2}}\frac{\hat{R}}{R^2},\quad \vec{B}(t)=\frac{1}{c^2}\vec{v}\times\vec{E}(t),
$$
其中$\vec{R}=R\hat{R}=(d,0,vt)$, $\sin\theta=d/R$,  电磁场写为分量形式为
$$
E_x=-\frac{e}{4\pi\epsilon_0}\frac{1-\beta^2}{(1-\beta^2\sin^2\theta)^{3/2}}\frac{d}{R^2},\quad E_y=0,\quad E_z=-\frac{e}{4\pi\epsilon_0}\frac{1-\beta^2}{(1-\beta^2\sin^2\theta)^{3/2}}\frac{vt}{R^2},\\
B_x=0,\quad B_y=\frac{v}{c^2}E_x,\quad B_z=0.
$$
取$d=1.0$m, $E_k=10$MeV, 则电磁场峰值分别为$E_{\max}=29.4$nV/m, $B_{\max}=1.0$pG; 如果是一个包含$10^{10}$个电子的束团，且空间分布可忽略，则峰值变为$E_{\max}=294$V/m, $B_{\max}=1.0\mathrm{\mu}$T; 图像如下：

<img src="D:\QY\定向能\粒子束\eBeamSGEMP\report\EM_field_pulses_single_electron.png" width=75% >

## 匀速运动的单电子束团产生的电磁场

对具有一定空间分布的电子束团，在线性叠加原理的假设下，其产生的电磁场显然可以通过对电荷密度积分得到。为简单起见，假设电子束团仅沿传输方向有密度分布$\lambda(z')$，可被视为一维，总电子数为$N$, 归一化要求
$$
eN=\int_{-v_0\tau_0}^{v_0\tau_0}\lambda(z')dz'
$$
其中$\tau_0$为电子束团脉宽，$v_0$为束团在实验室系中运动的平均速度。$z'$是束流共动参考系中的坐标，与实验室系中坐标换算关系为$z'=z-v_0t$, 忽略能散和散角，所有电子速度均为$v_0$，沿传输方向空间分布为均匀分布。则
$$
\lambda(z')=\frac{eN}{2v_0\tau_0},\quad -v_0\tau_0\leq z'\leq v_0\tau_0,
$$

$$
\vec{E}_{\text{pulse}}(t)=\int dz'\vec{E}(z',t),\quad \vec{B}_{\text{pulse}}(t)=\int dz'\vec{B}(z',t),
$$

其中
$$
\vec{E}(z',t)=-\frac{\lambda(z')}{4\pi\epsilon_0}\frac{1-\beta^2}{(1-\beta^2\sin^2\theta(z'))^{3/2}}\frac{\hat{R}(z')}{R(z')^2},\quad \vec{B}(z',t)=\frac{1}{c^2}\vec{v}\times\vec{E}(z',t),
$$
$\theta(z')=d/R(z')$, $\vec{R}(z')=R(z')\hat{R}(z')=(d,0,z'+vt)$, 取$d=1.0$m, $E_k=10$MeV, $N=10^{10}$, $\tau_0=100$ps, 数值积分可得



## 电磁场的卷积形式重构

### 核心观点

在固定探测点 $(d,0,0)$ 处测量到的来自运动电荷分布的电磁场，可以表述为**电荷分布与单电子格林函数的卷积**：

$$
\vec{E}_{\text{pulse}}(t) = [\lambda * G_E](t), \quad \vec{B}_{\text{pulse}}(t) = [\lambda * G_B](t)
$$

其中卷积运算在时间域上进行，$G_E$ 和 $G_B$ 是单电子的电磁格林函数。

### 数学重构

我们定义单电子电磁响应函数。对于一个在 $t=0$ 时刻通过原点的电子：

**单电子格林函数：**
$$
G_E(t) = -\frac{e}{4\pi\epsilon_0} \frac{1-\beta^2}{(1-\beta^2\sin^2\theta(t))^{3/2}} \frac{\hat{R}(t)}{R(t)^2}
$$
其中 $\vec{R}(t) = (d, 0, v_0t)$，$R(t) = \sqrt{d^2 + (v_0t)^2}$，$\sin\theta(t) = d/R(t)$

**时间域电荷分布：**
由于 $z' = z - v_0t$，时间域电荷分布为：
$$
\lambda(t) = \frac{eN}{2\tau_0} \cdot \text{rect}\left(\frac{t}{\tau_0}\right)
$$
其中 $\text{rect}(x) = 1$（当 $|x| \leq \frac{1}{2}$），否则为 $0$。

**卷积表示：**
$$
\vec{E}_{\text{pulse}}(t) = \int_{-\infty}^{\infty} \lambda(\tau) G_E(t - \tau) d\tau = \frac{eN}{2\tau_0} \int_{-\tau_0/2}^{\tau_0/2} G_E(t - \tau) d\tau
$$

### 物理解释

1. **线性时不变系统视角**：真空可视为一个线性系统，其中：
   - **输入**：时间域电荷分布 $\lambda(t)$
   - **冲激响应**：单电子场 $G_E(t)$
   - **输出**：测量到的总场 $\vec{E}_{\text{pulse}}(t)$

2. **因果性与传播**：卷积自然地编码了来自不同位置电子的场在不同时间到达探测器的效应。

3. **频域解释**：通过傅里叶变换，我们得到：
   $$
   \tilde{E}_{\text{pulse}}(\omega) = \tilde{\lambda}(\omega) \cdot \tilde{G}_E(\omega)
   $$
   其中 $\tilde{\lambda}(\omega) = eN \cdot \text{sinc}(\omega\tau_0/2)$ 是矩形脉冲的傅里叶变换。

### 此视角的优势

1. **计算效率**：可使用FFT方法快速计算卷积
2. **物理洞察**：将源特性与真空传播物理分离开来
3. **通用性**：易于推广到任意电荷分布 $\lambda(t)$
4. **系统分析**：支持使用信号处理工具（滤波、带宽分析等）

### 特殊情况：超相对论极限

当 $\beta \to 1$ 时，单电子场变得高度局域化，卷积近似于电荷分布的微分，这解释了为什么短束团在高频段辐射强烈。

这种卷积框架为束流电动力学提供了一个强大的信号处理视角，自然地连接到加速器物理中使用的阻抗概念和频域分析。