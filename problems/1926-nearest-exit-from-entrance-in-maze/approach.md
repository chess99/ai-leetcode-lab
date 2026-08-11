# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
从入口 BFS，首次走到非入口边界空格即最短出口。
## 正确性
BFS 按步数递增访问，首次出口距离最小。
## 复杂度
时间空间 `O(mn)`。
## 边界条件与本地验证
- 入口不算出口；验证无出口。
