# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

转换为数组，用递减下标栈在遇到更大值时填充答案。

## 复杂度

时间空间 `O(n)`。

## 边界条件与本地验证

- 无更大值保留零；已完成 `py_compile` 和断言。
