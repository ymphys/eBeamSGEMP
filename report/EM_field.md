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

对具有一定空间分布的电子束团，在线性叠加原理的假设下，其产生的电磁场显然可以通过对电荷密度积分得到。为简单起见，假设电子束团仅沿传输方向有密度分布，可被视为一维，总电子数为$N$,
$$
N=\int_{-v\tau_0}^{v\tau_0}\lambda(z',t=0)dz'
$$
则
$$
\vec{E}_{\text{pulse}}(t)=\int dz'\vec{E}(z',t),\quad \vec{B}_{\text{pulse}}(t)=\int dz'\vec{B}(z',t),
$$
