# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

生成不超过剩余和的最大 Fibonacci 数，贪心选取并继续处理剩余值。Zeckendorf 定理保证该贪心取得最少数量。

## 复杂度

时间 `O(log k)`，空间 `O(1)`。

## 边界条件与本地验证

- 验证了 `k=1`、Fibonacci 数和非 Fibonacci 数。
