# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
顺序枚举 n 的因子，数到第 k 个即返回。
## 复杂度
时间 `O(N)`，空间 `O(1)`。
## 边界条件与本地验证
因子不足 k 个返回 -1。
