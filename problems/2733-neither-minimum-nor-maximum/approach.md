# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

少于三个元素时不存在答案。否则排序后第二小的元素既不是最小值，也不是最大值。

## 复杂度

时间复杂度 O(n log n)，额外空间复杂度 O(n)。

## 边界条件与本地验证

数组长度为 1 或 2 时返回 -1。已进行 Python 语法检查及样例断言。
