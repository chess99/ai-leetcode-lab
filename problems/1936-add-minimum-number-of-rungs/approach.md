# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

逐段计算相邻横档间距，间距为 gap 时需补 `(gap-1)//dist` 个横档。

## 正确性

每个新增横档最多缩短 dist，公式给出使该段每跳不超过 dist 的最少数量，各段独立可加。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

首段从高度 0 起算；刚好等于 dist 不需补。已用样例验证。
