# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
按层 BFS 找到恰好 `level` 层的朋友，统计其视频频次并按频次、名称排序。
## 复杂度
时间 `O(V+E+W log W)`，空间 `O(V+W)`。
## 边界条件与本地验证
覆盖题面层级示例。
