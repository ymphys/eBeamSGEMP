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
E_x=-\frac{e}{4\pi\epsilon_0}\frac{1-\beta^2}{(1-\beta^2\sin^2\theta)^{3/2}}\frac{d}{R^3},\quad E_y=0,\quad E_z=-\frac{e}{4\pi\epsilon_0}\frac{1-\beta^2}{(1-\beta^2\sin^2\theta)^{3/2}}\frac{vt}{R^3},\\
B_x=0,\quad B_y=\frac{v}{c^2}E_x,\quad B_z=0.
$$
经化简可得
$$
E_x(t)=-\frac{e\gamma}{4\pi\epsilon_0d^2}\frac{1}{(1+(\beta\gamma t/t_0)^2)^{3/2}},\quad E_z(t)=\frac{\beta t}{t_0}E_x(t),\quad t_0=\frac{d}{c},\\
$$
则电场幅度的峰值和半高全宽为
$$
|E|_{\max}=-\frac{e\gamma}{4\pi\epsilon_0d^2}, \tau_E=2(2^{2/3}-1)^{1/2}\frac{t_0}{\beta\gamma},
$$
取$d=1.0$m, $E_k=10$MeV, 则电磁场峰值分别为$E_{\max}=29.4$nV/m, $B_{\max}=1.0$pG; 如果是一个包含$10^{10}$个电子的束团，且空间分布可忽略，则峰值变为$E_{\max}=294$V/m, $B_{\max}=1.0\mathrm{\mu}$T; FWHM=248ps, 图像如下：

<img src="D:\QY\定向能\粒子束\eBeamSGEMP\report\single_electron_em_fields.png" width=75% >

## 匀速运动的单电子束团产生的电磁场

对具有一定空间分布的电子束团，在线性叠加原理的假设下，其产生的电磁场显然可以通过对电荷密度积分得到。为简单起见，假设电子束团仅沿传输方向有密度分布$\lambda(z')$，可被视为一维，总电子数为$N$, 归一化要求
$$
eN=\int_{-\infty}^{\infty}\lambda(z')dz',\quad \lambda(z')=\frac{eN}{2v_0\tau_0}\text{rect}(\frac{z'}{2v_0\tau_0}),
$$
其中$\tau_0$为电子束团脉宽，$v_0$为束团在实验室系中运动的平均速度。$z'$是束流共动参考系中的坐标，与实验室系中坐标换算关系为$z'=z-v_0t$, 初始条件为$t=0,z'=z\in(-v_0\tau_0,v_0\tau_0)$。忽略能散和散角，所有电子速度均为$v_0$，沿传输方向空间分布为均匀分布。则电磁场变为
$$
\vec{E}_{\text{pulse}}(t)=\int dz'\vec{E}(z',t),\quad \vec{B}_{\text{pulse}}(t)=\int dz'\vec{B}(z',t),
$$

其中
$$
\vec{E}(z',t)=-\frac{\lambda(z')}{4\pi\epsilon_0}\frac{1-\beta^2}{(1-\beta^2\sin^2\theta(z'))^{3/2}}\frac{\hat{R}(z')}{R(z')^2},\quad \vec{B}(z',t)=\frac{1}{c^2}\vec{v}\times\vec{E}(z',t),
$$
$\theta(z')=d/R(z')$, $\vec{R}(z')=R(z')\hat{R}(z')=(d,0,z'+vt)$, 取$d=1.0$m, $E_k=10$MeV, $N=10^{10}$, $\tau_0=100$ps, 数值积分可得, $E_{\max}=252$V/m, $B_{\max}=0.8\mathrm{\mu}$T, FWHM=309ps; 图像如下： 

<img src="D:\QY\定向能\粒子束\eBeamSGEMP\report\micropulse_EM_field.png" width=75% >

若取$\tau_0=$150ps, 则$E_{\max}=218$V/m, $B_{\max}=0.7\mathrm{\mu}$T, FWHM=374ps; 图像如下：

<img src="D:\QY\定向能\粒子束\eBeamSGEMP\report\micropulse_150ps.png" width=75% >

### 信号处理视角

在上面的积分中，做变量替换$z'=v_0\tau$可得
$$
eN=v_0\int_{-\infty}^{\infty}\lambda(\tau)d\tau,\quad \lambda(\tau)=\frac{eN}{2v_0\tau_0}\text{rect}(\frac{\tau}{2\tau_0}),
$$
其中$\tau$是束团内参考时间，$\tau=0$代表束团中心。此时固定探测点 $(d,0,0)$ 处测量到的电磁场为：
$$
\vec{E}_{\text{pulse}}(t)=v_0\int d\tau\vec{E}(\tau,t),\quad
\vec{E}(\tau,t)=-\frac{\lambda(\tau)}{4\pi\epsilon_0}\frac{1-\beta^2}{(1-\beta^2\sin^2\theta(\tau,t))^{3/2}}\frac{\hat{R}(\tau,t)}{R(\tau,t)^2},
$$

而$\vec{R}(\tau,t)=(d,0,v_0\tau+v_0t)=\vec{R}(t+\tau)$, 因此$\vec{E}(\tau,t)=\lambda(\tau)\vec{E}(t+\tau)/e,$
$$
\quad\vec{E}_{\text{pulse}}(t)=\frac{v_0}{e}\int_{-\infty}^{\infty} d\tau\lambda(\tau)\vec{E}(\tau+t)=\frac{v_0}{e}(\lambda\star\vec{E}),
$$
即**微脉冲电子束团产生的电磁脉冲是单电子电磁脉冲与束团分布的交叉相关**。

对矩形函数，上述交叉相关有解析解，这里给出电场脉冲的分量形式
$$
\begin{aligned}
E_{\text{pulse}-x}(t)
&=-\frac{Ne\gamma}{4\pi\epsilon_0d^2}\frac{1}{2\tau_0}\int_{-\infty}^{\infty} d\tau\ \text{rect}(\frac{\tau}{2\tau_0})\frac{1}{[1+\beta^2\gamma^2(\tau+t)^2/t_0^2]^{3/2}}\\
&=-\frac{Ne\gamma}{4\pi\epsilon_0d^2}\left(\dfrac{t+\tau_0}{2\tau_0}\frac{1}{\sqrt{1+\beta^2\gamma^2(t+\tau_0)^2/t_0^2}}+(t\to-t)\right)
\end{aligned}
$$

$$
\begin{aligned}
E_{\text{pulse}-z}(t)
&=-\frac{Ne}{4\pi\epsilon_0d^2}\frac{\beta\gamma}{2t_0\tau_0}\int_{-\infty}^{\infty} d\tau\ \text{rect}(\frac{\tau}{2\tau_0})\frac{\tau+t}{[1+\beta^2\gamma^2(\tau+t)^2/t_0^2]^{3/2}}\\
&=-\frac{Ne}{4\pi\epsilon_0d^2}\frac{t_0}{2\beta\gamma\tau_0}\left(\frac{1}{\sqrt{1+\beta^2\gamma^2(t-\tau_0)^2/t_0^2}}-(t\to-t)\right)
\end{aligned}
$$

可以看出，电场脉冲的x分量关于t=0是对称的，而z分量是反对称的；x分量被洛伦兹因子$\gamma$增强，而z分量被压低，这与单电子情形一致。电场脉冲的峰值和半高全宽为
$$
|E|_{\max}=-\frac{Ne\gamma}{4\pi\epsilon_0d^2}\frac{1}{\sqrt{1+\beta^2\gamma^2r_\tau^2}},\\ 
\tau_E\approx2\tau_0+2\tau_0\frac{(1+4\beta^2\gamma^2r_\tau^2)}{(1+4\beta^2\gamma^2r_\tau^2)^{3/2}-1}\left(2-\sqrt{\frac{1+4\beta^2\gamma^2r_\tau^2}{1+\beta^2\gamma^2r_\tau^2}}\right)
$$
其中$\tau_E$是在$t=\tau_0$附近展开取得的，$r_\tau=\tau_0/t_0$, 取$d=1.0$m, $E_k=10$MeV, $N=10^{10}$, $\tau_0=100$ps, 可得$E_{\max}=252$V/m, FWHM=309ps，与上文结果一致；取短/长束团极限可得
$$
\begin{aligned}
&|E|_{\max}=-\frac{e}{4\pi\epsilon_0d}\frac{N}{v_0\tau_0},\quad\tau_E=2\tau_0+\frac{3t_0^3}{4\beta^3\gamma^3\tau_0^2},\quad\tau_0\gg t_0,\\
&|E|_{\max}=-\frac{Ne\gamma}{4\pi\epsilon_0d^2}(1-\frac{\beta^2\gamma^2\tau_0^2}{2t_0^2}),\quad\tau_E=2\tau_0+\frac{t_0^2}{3\beta^2\gamma^2\tau_0},\quad\gamma\tau_0\ll t_0,
\end{aligned}
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