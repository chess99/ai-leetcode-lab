# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

遍历数组，计算每个下标二进制表示中 1 的数量，符合 k 的下标对应值计入总和。

## 复杂度

时间复杂度 O(n log n)，额外空间复杂度 O(1)。

## 边界条件与本地验证

下标 0 的置位数为 0。已进行 Python 语法检查及样例断言。
