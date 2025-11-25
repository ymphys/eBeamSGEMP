````markdown
# Prompt for Codex: Generate `micropulse.py`

## Overview
编写一个 Python 程序 `micropulse.py`，用于计算 **匀速运动的一维均匀电子束团** 在观察点产生的 **时域电磁场脉冲**。程序需要根据给定物理模型对束团内部每个电子位置进行积分，并计算时间区间内的电场与磁场波形。

## Physical Model Summary (for coding)
1. 束团沿 **z 方向匀速运动**，速度为  
   \[
   v_0 = \beta c,\quad E_k=10\text{ MeV}
   \]
2. 束团空间分布为 **一维均匀分布**：  
   \[
   \lambda(z')=\frac{eN}{2v_0\tau_0},\quad z'\in[-v_0\tau_0, v_0\tau_0]
   \]
3. 坐标转换：  
   \[
   z' = z - v_0 t
   \]
4. 单电子在观察点产生的电磁场：
   - 观察点设置为  
     \[
     \vec R(z') = (d,\,0,\,z' + v_0 t),\quad d=1.0\text{ m}
     \]
   - 距离  
     \[
     R = \sqrt{d^2+(z'+v_0 t)^2}
     \]
   - 视角  
     \[
     \theta = d/R
     \]
   - 电场  
     \[
     \vec E(z',t)= -\frac{\lambda(z')}{4\pi\epsilon_0}\frac{1-\beta^2}{(1-\beta^2\sin^2\theta)^{3/2}}\frac{\hat R}{R^2}
     \]
   - 磁场  
     \[
     \vec B(z',t)= \frac{1}{c^2} \vec v \times \vec E
     \]
5. 束团电磁场为积分：
   \[
   \vec{E}_\text{pulse}(t)=\int dz'\,\vec E(z',t),\quad
   \vec{B}_\text{pulse}(t)=\int dz'\,\vec B(z',t)
   \]
6. 需要计算时间区间：
   \[
   t\in[-1\times10^8,\;1\times10^8]\text{（单位：秒）}
   \]

## Coding Requirements
1. **程序结构**
   - 生成 `micropulse.py`
   - 主程序应执行以下步骤：
     - 定义全部常数
     - 计算 relativistic β
     - 生成 z′ 网格
     - 对每个 t 计算 E、B 的积分
     - 存储 E(t)、B(t)
     - 绘制波形图

2. **数值方法**
   - z′ 使用 **均匀网格**，点数可设置为 2000–5000，可通过变量配置。
   - t 网格可设为 3000–5000 个点。
   - 使用 `numpy` 和 `scipy` 进行积分与向量运算。
   - 所有结果使用 SI 单位。

3. **可视化**
   - 使用 `matplotlib`
   - 绘制：
     - Ex(t)
     - Ez(t)
     - |E|(t)
     - 以及对应磁场分量

4. **代码质量要求**
   - 写明注释和公式来源
   - 清晰的函数结构，例如：
     - `compute_single_E(zp, t)`
     - `compute_pulse_E(t)`
     - `main()`
   - 保证程序可以直接执行并生成图像文件

5. **输出**
   - 当运行 `python micropulse.py` 时，应输出：
     - 电场波形图 `E_pulse.png`
     - 磁场波形图 `B_pulse.png`
     - 控制台打印关键参数（β、γ、峰值场强等）

## Program Skeleton (Codex Should Flesh Out)
Codex 应使用以下框架生成完整代码：

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, elementary_charge as e

# define constants ...
# lambda ...
# compute single-particle field ...
# integrate over z' ...
# loop over t ...
# plot ...
````

## Final Deliverables

Codex 必须输出一个可直接运行的单文件 Python 程序 `micropulse.py`，实现：

* 计算均匀电子束团在观察点随时间的电磁场
* 完成对 z′ 的数值积分
* 生成电磁脉冲波形图
* 代码结构清晰、带注释、可复现

确保输出中不包含其他文件，所有内容均写入 `micropulse.py`。

```markdown
```
