# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

路径长度为 `d`。权重为 1 的边数量须为奇数；在全部 `2^d` 种赋值中奇偶两类各占一半，因此 `d>0` 时答案为 `2^(d-1)`，零长度路径为零。倍增 LCA 求每条路径长度。

## 复杂度

预处理 `O(n log n)`，每次查询 `O(log n)`，空间 `O(n log n)`。

## 边界条件与本地验证

处理 `u=v`、单边路径和模幂计算。
