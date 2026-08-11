# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
`dp[i]` 为和为 i 的最少平方数，对所有不大于 i 的平方 j² 取 `dp[i-j²]+1` 最小值。
## 复杂度
- 时间 O(n√n)，空间 O(n)。
## 边界条件与本地验证
- 完全平方数答案为 1。验证 `12 -> 3`、`13 -> 2`、`1 -> 1`。
