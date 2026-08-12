# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

记录调用的时间严格递增，因此把时间直接追加到有序数组，并同步维护分数前缀和。查询时分别二分出第一个不小于 `startTime` 和第一个大于 `endTime` 的位置，两前缀和相减。

## 复杂度

`record` 时间 `O(1)`，`totalScore` 时间 `O(log n)`，空间 `O(n)`。

## 边界条件与本地验证

查询区间两端都包含；没有考试时二分边界相同，结果自然为 0。按题面完整调用序列验证所有返回值；`record` 中按题意保留中间输入变量。
