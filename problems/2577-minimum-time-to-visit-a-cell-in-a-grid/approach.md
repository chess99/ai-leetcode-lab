# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
用 Dijkstra 求最早到达时间；若必须等待，利用往返一步调整时间奇偶。
## 复杂度
时间 O(mn log(mn))，空间 O(mn)。
## 边界条件与本地验证
起点无法迈出时返回负一；小网格按时间 BFS 核对。
