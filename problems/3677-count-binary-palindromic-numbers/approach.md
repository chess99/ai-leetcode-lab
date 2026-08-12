# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

先计更短长度的二进制回文，再枚举当前长度的前半部分并镜像，比较不超过上界的数量。

## 复杂度

时间 `O(log n)`，空间 `O(1)`。

## 边界条件与本地验证

已对 `n<1000` 逐个判回文对拍。
