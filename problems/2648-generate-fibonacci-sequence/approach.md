# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

维护相邻两项 `a`、`b`。每次产出 `a` 后，同时更新为下一对相邻斐波那契数。

## 复杂度

每次 `next()` 的时间复杂度为 O(1)，额外空间复杂度为 O(1)。

## 边界条件与本地验证

从 0、1 开始，生成器可无限产出。已进行 JavaScript 语法检查及前几项样例断言。
