# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

构建前缀和 `prefix`，其中 `prefix[i]` 是前 `i` 个单词中首尾均为元音的数量。每个闭区间 `[l, r]` 的答案为 `prefix[r + 1] - prefix[l]`。

## 复杂度

预处理时间和空间均为 `O(n)`；每个查询时间 `O(1)`，返回数组额外占 `O(q)`。

## 边界条件与本地验证

长度为一的元音单词同样满足条件；查询可覆盖整个数组或只包含一个单词。
