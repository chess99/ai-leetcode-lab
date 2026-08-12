# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

维护有序已占座位，遍历首端、相邻间隔和末端，选最大距离且最小下标；离开时删除。

## 复杂度

seat 时间 `O(n)`，leave `O(n)`，存储 `O(n)`。

## 边界条件与本地验证

- 同距保留较小下标；本地 `py_compile` 和操作序列断言通过。
