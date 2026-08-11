# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

二分水平线高度，以所有正方形线下面积之和判断方向。

## 复杂度

时间 `O(n log 精度)`，空间 `O(1)`。

## 边界条件与本地验证

覆盖重叠面积重复计数及面积相等的平台。
