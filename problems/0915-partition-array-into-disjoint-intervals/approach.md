# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

扫描维护左部分最大值及已扫描最大值；当前值小于左最大值时必须扩展左部分。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

- 已完成 `py_compile` 和多次扩展断言。
