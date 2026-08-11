# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

区间动态规划枚举两端是否配对，配对消耗两字符循环字母表距离。

## 复杂度

时间 `O(n^2k)`，空间 `O(n^2k)`。

## 边界条件与本地验证

覆盖首尾跨越 z/a 的距离。
