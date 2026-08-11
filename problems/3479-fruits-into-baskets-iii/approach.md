# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

线段树维护未使用篮子的区间最大容量，向左优先下降找到最左可用篮子。

## 复杂度

时间 `O(n log n)`，空间 `O(n)`。

## 边界条件与本地验证

覆盖无可用篮子和最左篮子选择。
