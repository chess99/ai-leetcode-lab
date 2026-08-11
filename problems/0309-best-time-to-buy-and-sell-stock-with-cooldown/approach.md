# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
滚动维护持有、刚卖出、可买三种状态。
## 复杂度
- 时间 O(n)，空间 O(1)。
## 边界条件与本地验证
- 单日利润为零。验证 `[1,2,3,0,2] -> 3`。
