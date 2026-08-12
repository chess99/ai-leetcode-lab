# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
从每个节点 BFS，遇到非父边即形成环并更新最短长度。
## 复杂度
时间 O(V(V+E))，空间 O(V+E)。
## 边界条件与本地验证
无环返回负一；小图枚举简单环核对。
