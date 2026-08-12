# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
区间 DP 枚举首次猜测，取最小最坏成本。
## 复杂度
- 时间 O(n³)，空间 O(n²)。
## 边界条件与本地验证
- 单数区间成本为零。验证 `10 -> 16`，并与独立记忆化 minimax 对拍 `n=1..15`。
