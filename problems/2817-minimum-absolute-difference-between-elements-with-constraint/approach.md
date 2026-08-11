# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
坐标压缩配合 Fenwick 树维护所有合法左侧值，查询当前值的前驱和后继。
## 复杂度
时间 `O(n log n)`，空间 `O(n)`。
## 边界条件与本地验证
`x=0` 答案为 0；已验证题面样例。
