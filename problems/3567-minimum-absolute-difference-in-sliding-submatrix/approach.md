# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

枚举每个 k×k 窗口，取其中不同数值排序，答案是相邻有序值差的最小值。

## 复杂度

时间 O((m-k+1)(n-k+1)k²log k)，给定 30×30 的上界足够；没有不同值时为 0。

## 边界条件与本地验证

待填写。
