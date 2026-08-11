# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

将 `(value, label)` 按 value 从大到小排序，依次尝试选择。仅当该标签已选数量小于 `useLimit` 时才计入答案，选满 `numWanted` 后结束。由于处理顺序始终是当前可选项中的最大 value，贪心选择不会劣于跳过它而改选更小的项。

## 复杂度

排序耗时 `O(n log n)`，扫描耗时 `O(n)`；哈希表额外空间为 `O(n)`。

## 边界条件与本地验证

同一标签达到上限后继续扫描其他标签；允许选不到 `numWanted` 项时返回可选项总和。已用题目三个样例验证。
