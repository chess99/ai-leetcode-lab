# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

每个值的深度只在 0 至 5。为每个深度维护一棵 Fenwick 树，更新时删旧加新，区间查询做前缀差。

## 复杂度

每次操作 `O(log n)`，空间 `O(n)`。

## 边界条件与本地验证

处理值一和深度零；覆盖更新为相同深度。
