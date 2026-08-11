# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
按双方价值和降序取石头，轮流累加 Alice 分数和扣除 Bob 分数。
## 正确性
价值和最大石头的优先选择同时最大化己方收益与对方机会成本，标准贪心最优。
## 复杂度
时间 `O(n log n)`，空间 `O(n)`。
## 边界条件与本地验证
- 验证了胜、负和同分。
