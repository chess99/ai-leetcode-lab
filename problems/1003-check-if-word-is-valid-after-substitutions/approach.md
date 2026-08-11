# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

栈模拟删除：每次压入字符，末尾出现 `abc` 就立即删除，最终栈空即合法。

## 复杂度

时间空间 `O(n)`。

## 边界条件与本地验证

- 已完成 `py_compile` 和嵌套/非法断言。
