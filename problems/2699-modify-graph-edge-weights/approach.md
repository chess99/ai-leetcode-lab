# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
先以未知边为一求到终点下界。正向 Dijkstra 遇到未知边时按目标距离补足权重，最后验证。
## 复杂度
时间 O((V+E) log V)，空间 O(V+E)。
## 边界条件与本地验证
下界已超过目标即失败；小图枚举未知权重核对。
