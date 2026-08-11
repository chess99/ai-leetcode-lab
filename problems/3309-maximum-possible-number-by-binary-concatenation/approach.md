# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

将每个数转换为二进制字符串，按 `a+b` 与 `b+a` 的较大者优先排序，再拼接并转回整数。

## 复杂度

时间 `O(n log n * L)`，空间 `O(nL)`，其中 `L` 为二进制位数。

## 边界条件与本地验证

覆盖拼接顺序不同和比较结果相等。
