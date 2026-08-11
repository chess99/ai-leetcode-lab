# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

用闭包保存当前计数。三个方法分别对该状态自增、自减，或恢复为初始值。

## 复杂度

每次调用的时间复杂度和额外空间复杂度均为 O(1)。

## 边界条件与本地验证

`reset` 始终恢复创建时的初值。已进行 JavaScript 语法检查及方法调用断言。
