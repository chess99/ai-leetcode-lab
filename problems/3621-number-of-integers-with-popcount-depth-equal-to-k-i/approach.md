# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

按二进制一的数量分类，组合计数不超过 `n` 的数字；一数量的递归深度预处理即可。

## 复杂度

时间和空间均为 `O(log^2 n)`。

## 边界条件与本地验证

单独处理 `x=1` 的深度零。
