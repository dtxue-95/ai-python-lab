import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# ==================== 已知数据 ====================
mean = 24.97
std = 0.1494
LSL = 24.5
Target = 25.0
USL = 25.5
Cp = 1.12
Cpk = 1.05

# ==================== 需要你填入的样本量 ====================
n = 30   # ← 请根据实际样本量修改（无此值无法计算置信区间）

# 计算 95% 置信区间
se = std / np.sqrt(n)
t_crit = t.ppf(0.975, n-1)
ci_lower = mean - t_crit * se
ci_upper = mean + t_crit * se

# ==================== 绘图 ====================
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制均值点
x_pos = [0]
ax.scatter(x_pos, mean, color='red', s=80, zorder=3, label='Mean')

# 绘制置信区间误差线
ax.errorbar(x_pos, mean,
            yerr=[[mean - ci_lower], [ci_upper - mean]],
            fmt='none', ecolor='black', capsize=8, capthick=2, elinewidth=2,
            label=f'95% CI (n={n})')

# 规格限与目标线
ax.axhline(LSL, color='blue', linestyle='--', linewidth=1.5, label=f'LSL = {LSL}')
ax.axhline(Target, color='green', linestyle='-', linewidth=1.5, label=f'Target = {Target}')
ax.axhline(USL, color='blue', linestyle='--', linewidth=1.5, label=f'USL = {USL}')

# 坐标轴设置
ax.set_xticks(x_pos)
ax.set_xticklabels(['New Process'])
ax.set_ylabel('Measurement')
ax.set_title('Interval Plot (95% CI) for New Process')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# 添加 Cp / Cpk 信息
text_str = f'New Process:\nCp = {Cp}\nCpk = {Cpk}'
ax.text(0.98, 0.05, text_str, transform=ax.transAxes,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()