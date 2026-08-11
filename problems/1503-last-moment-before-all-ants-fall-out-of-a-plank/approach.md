# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

相遇后掉头等价于两只蚂蚁交换身份，因此只看各自直行的掉落时间。向左蚂蚁耗时为位置，向右蚂蚁为 `n - 位置`，取最大值。

## 复杂度

时间 `O(left.length + right.length)`，额外空间 `O(1)`。

## 边界条件与本地验证

任一方向可为空。已用题目三个样例验证。
