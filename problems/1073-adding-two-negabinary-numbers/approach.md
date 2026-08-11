# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

从低位相加，当前位取奇偶，负二进制进位为负的半数。

## 复杂度

时间空间 `O(n)`。

## 边界条件与本地验证

- 去除高位零；完成 `py_compile` 和断言。
