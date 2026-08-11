# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
顺序维护当前胜者及连胜次数；最大元素最终必胜。
## 复杂度
时间 `O(N)`，空间 `O(1)`。
## 边界条件与本地验证
覆盖 k 很大时返回全局最大值。
