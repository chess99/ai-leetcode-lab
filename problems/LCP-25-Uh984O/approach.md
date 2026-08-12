# 解题记录

- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium；轮次：1

## 思路

逐个加入 26 个字母。`dp[length]` 表示已处理字母组成长度 length 字符串的方案数；当前字母使用 count 次时，可插入到新串的 `C(length+count, count)` 组位置中，且 `0 <= count <= k`。

## 复杂度

时间 `O(26*N*k)`，空间 `O(N)`。

## 边界条件与本地验证

覆盖 n 超过 26k 时自然得到 0（题面保证范围内）、count 为 0 和模运算。官方样例 26、650 均通过。
