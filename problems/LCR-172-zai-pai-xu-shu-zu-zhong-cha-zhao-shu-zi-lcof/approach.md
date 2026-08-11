# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

分别二分查找第一个不小于 `target` 与第一个不小于 `target + 1` 的位置，二者差值就是目标次数。

## 复杂度

时间复杂度为 `O(log n)`，额外空间复杂度为 `O(1)`。

## 边界条件与本地验证

目标不存在时两个边界相同；本地断言覆盖两个样例。
