# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

扫描排列并维护前缀最大值；当最大值等于当前位置时，前缀恰包含该范围全部数值，可切分一块。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

- 本地 `py_compile` 和单块/多块断言通过。
