# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
尽量拆成 3，末尾剩 4 时保留为 2×2，最大化乘积。
## 复杂度
- 时间 O(n)，空间 O(1)。
## 边界条件与本地验证
- n≤3 必须至少拆分一次。验证 `2 -> 1`、`10 -> 36`。
