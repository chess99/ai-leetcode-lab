# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

维护三个独立的栈，并为每个栈限制容量。满栈时忽略 push，空栈的 pop 和 peek 返回 -1。

## 复杂度

每个操作的时间复杂度均为 O(1)，额外空间复杂度 O(3×stackSize)。

## 边界条件与本地验证

容量为 0 时所有 push 都被忽略。已进行 Python 语法检查及最小断言。
