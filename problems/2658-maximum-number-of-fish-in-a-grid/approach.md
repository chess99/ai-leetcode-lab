# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
对每个未访问的正数格做迭代 DFS，累加连通分量鱼数并记录最大值。
## 复杂度
时间 `O(mn)`，空间 `O(mn)` 最坏。
## 边界条件与本地验证
搜索后原地置零避免重复；全零网格返回 0。已验证题面样例。
