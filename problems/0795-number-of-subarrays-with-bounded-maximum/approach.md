# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

答案等于最大值不超过 right 的子数组数减去最大值不超过 left-1 的子数组数。扫描时累计每段连续满足上界的长度。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

- 已完成 `py_compile` 和示例/边界断言。
