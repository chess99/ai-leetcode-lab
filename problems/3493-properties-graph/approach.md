# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

两两比较去重后的属性交集，达到阈值即用并查集合并。

## 复杂度

时间 `O(n^2m)`，空间 `O(nm)`。

## 边界条件与本地验证

覆盖重复属性不重复计数。
