# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
行列各维护可到达范围的最小堆，按行列扫描时弹出已过期范围并取得最少步数。
## 复杂度
时间 O(mn log(mn))，空间 O(mn)。
## 边界条件与本地验证
不可达返回负一；小网格 BFS 核对。
