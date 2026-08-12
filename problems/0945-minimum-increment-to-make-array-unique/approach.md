# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

排序后每个数至少为前数加一，不足则递增并累计差值。

## 复杂度

时间 `O(n log n)`，空间取决于排序。

## 边界条件与本地验证

- 重复和连续碰撞均覆盖；已完成 `py_compile` 和断言。
