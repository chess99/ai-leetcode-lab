# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
`dp[t]` 累加各候选数作为末尾的有序组合。
## 复杂度
- 时间 O(target·n)，空间 O(target)。
## 边界条件与本地验证
- `dp[0]=1`，表示组成 0 的空序列。验证 `[1,2,3],4 -> 7`，并与独立记忆化递归对拍 500 组随机输入。
