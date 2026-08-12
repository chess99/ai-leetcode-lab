# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
按题型做有数量上限的背包，转移选取零到给定数量道题。
## 复杂度
时间 O(target·总数量)，空间 O(target)。
## 边界条件与本地验证
分数恰好目标；枚举小题型取数核对。
