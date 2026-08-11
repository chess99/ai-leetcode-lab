# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

反复对负二做带非负余数的除法，余数逆序即表示。

## 复杂度

时间和空间 `O(log n)`。

## 边界条件与本地验证

- 零单独返回；已完成 `py_compile` 和断言。
