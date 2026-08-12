# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

敌人 `i` 需要 `ceil(health[i]/power)` 次攻击。若先杀 `i` 再杀 `j`，两者的顺序代价比较化为 `time_i*damage_j` 与 `time_j*damage_i`，据此用交叉乘法排序（Smith 规则）。按顺序击杀时累计当前所有存活敌人的总伤害。

## 复杂度

排序时间 `O(n log n)`，空间 `O(n)`。

## 边界条件与本地验证

交叉乘法避免浮点比值误差；单敌人和相同比值自然处理。3 组样例与 `n<=8` 全排列 oracle 通过，10 万敌人约 0.30 秒。
