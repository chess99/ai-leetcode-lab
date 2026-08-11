# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

分别收集左下和右上起点的主对角线，按题意排序后写回。

## 复杂度

时间 `O(n^2 log n)`，空间 `O(n)`。

## 边界条件与本地验证

覆盖单元素矩阵和题面示例。
