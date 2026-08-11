# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

用前缀和和分组动态规划，维护允许开新段位置的最大转移值。

## 复杂度

时间 `O(nk)`，空间 `O(n)`。

## 边界条件与本地验证

覆盖全负数和长度恰为 m。
