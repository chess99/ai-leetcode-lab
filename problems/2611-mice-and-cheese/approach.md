# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

先假定全部奶酪由第二只老鼠吃，得到 `sum(reward2)`。将第 `i` 块改给第一只老鼠带来的增益是 `reward1[i] - reward2[i]`，因此选择增益最大的 `k` 块即可。

## 复杂度

排序增益为 `O(n log n)` 时间，额外空间 `O(n)`。

## 边界条件与本地验证

`k = 0` 时保留基准分数；`k = n` 时所有奶酪都交给第一只老鼠。即使增益为负，也必须选择恰好 `k` 块。
