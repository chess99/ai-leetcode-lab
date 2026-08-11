# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
构建管理树并 BFS，队列携带收到通知的累计时间，取最大值。
## 复杂度
时间和空间均为 `O(N)`。
## 边界条件与本地验证
覆盖单员工与多层管理树。
