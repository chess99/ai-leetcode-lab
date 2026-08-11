# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
统计每行末尾零数，逐行向下寻找满足要求的最近行并用相邻交换上移。
## 复杂度
时间 `O(N²)`，空间 `O(N)`。
## 边界条件与本地验证
无可用行时返回 -1。
