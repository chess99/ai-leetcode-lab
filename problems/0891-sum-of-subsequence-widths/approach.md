# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

排序后 nums[i] 作为最大和最小各出现 2^i 与 2^(n-1-i) 次，按贡献相减累加。

## 复杂度

排序 O(n log n)，额外空间 O(1)。

## 边界条件与本地验证

按模数取结果；重复值贡献自然抵消。
