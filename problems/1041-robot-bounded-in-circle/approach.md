# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

模拟一轮指令。若回到原点或朝向改变，重复执行后必有界；否则无限远离。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

- 完成 `py_compile` 和有界/无界断言。
