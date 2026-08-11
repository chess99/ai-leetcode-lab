# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

统计各值频次。频次能被 k 整除时，将该值乘以其频次计入总和。

## 复杂度

时间复杂度 O(n)，额外空间复杂度 O(n)。

## 边界条件与本地验证

符合条件的值要按其出现次数重复计入。已进行 Python 语法检查及最小断言。
