import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# ==================== 数据设定 ====================
# 新过程（已知均值、标准差，假设样本量 n=30）
new_mean = 24.97
new_std = 0.1494
new_n = 30
new_se = new_std / np.sqrt(new_n)
new_t_crit = t.ppf(0.975, new_n - 1)       # 95% 置信区间的 t 值
new_ci_lower = new_mean - new_t_crit * new_se
new_ci_upper = new_mean + new_t_crit * new_se

# 旧过程（合理假设：均值稍低、波动稍大，样本量相同）
old_mean = 24.86
old_std = 0.18
old_n = 30
old_se = old_std / np.sqrt(old_n)
old_t_crit = t.ppf(0.975, old_n - 1)
old_ci_lower = old_mean - old_t_crit * old_se
old_ci_upper = old_mean + old_t_crit * old_se

# 规格限与目标
LSL = 24.5
Target = 25.0
USL = 25.5

# Cp / Cpk（仅用于标注）
Cp = 1.12
Cpk = 1.05

# ==================== 绘图 ====================
process_names = ['Old Process', 'New Process']
means = [old_mean, new_mean]
ci_low = [old_ci_lower, new_ci_lower]
ci_high = [old_ci_upper, new_ci_upper]

fig, ax = plt.subplots(figsize=(8, 6))

# 绘制均值点
x_pos = [0, 1]
ax.scatter(x_pos, means, color='red', zorder=3, label='Mean')

# 绘制置信区间误差线
ax.errorbar(x_pos, means,
            yerr=[[means[i]-ci_low[i] for i in range(2)],
                  [ci_high[i]-means[i] for i in range(2)]],
            fmt='none', ecolor='black', capsize=8, capthick=2, elinewidth=2,
            label='95% CI')

# 添加参考线
ax.axhline(LSL, color='blue', linestyle='--', linewidth=1.5, label=f'LSL = {LSL}')
ax.axhline(Target, color='green', linestyle='-', linewidth=1.5, label=f'Target = {Target}')
ax.axhline(USL, color='blue', linestyle='--', linewidth=1.5, label=f'USL = {USL}')

# 设置坐标轴
ax.set_xticks(x_pos)
ax.set_xticklabels(process_names)
ax.set_ylabel('Measurement')
ax.set_title('Interval Plot (95% CI) for 2-Sample t')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# 添加 Cp / Cpk 文本标注（放在图形空白处）
text_str = f'New Process:\nCp = {Cp}\nCpk = {Cpk}'
ax.text(0.98, 0.05, text_str, transform=ax.transAxes,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()