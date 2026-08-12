# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

树中连接三个指定点的最小子树权重等于三对距离之和除以二。预处理根到点距离和倍增 LCA，每个查询常数次 LCA 得到三段距离即可。

## 复杂度

预处理 `O(n log n)`，每个查询 `O(log n)`，空间 `O(n log n)`。

## 边界条件与本地验证

支持三点在同一路径及任意分叉位置；使用 64 位距离累加。
