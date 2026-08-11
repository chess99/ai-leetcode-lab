# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

二分比较中点与右邻居：上升则峰在右侧，否则峰在左侧含中点。

## 复杂度

时间 `O(log n)`，空间 `O(1)`。

## 边界条件与本地验证

- 本地 `py_compile` 和不同峰位断言通过。
