# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
滚动记录末尾上升和下降的最长长度。
## 复杂度
- 时间 O(n)，空间 O(1)。
## 边界条件与本地验证
- 相等值跳过。验证 `[1,7,4,9,2,5] -> 6`。
