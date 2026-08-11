# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

正反相同的数无论怎样翻转都会出现在正面，故全部禁用；其余正反面数均可能，取最小。

## 复杂度

时间和空间 `O(n)`。

## 边界条件与本地验证

- 没有候选返回零；已完成 `py_compile` 和示例断言。
