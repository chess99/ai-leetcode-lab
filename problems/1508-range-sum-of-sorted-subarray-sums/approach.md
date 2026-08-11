# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

枚举所有起点并向右累加生成所有子数组和，排序后按题目的 1-based 区间求和并取模。

## 复杂度

时间 `O(n^2 log n)`，空间 `O(n^2)`。

## 边界条件与本地验证

区间两端均包含。已用题目三个样例验证。
