# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
转换为集合，逐人检查是否为其他任一集合的子集。
## 复杂度
时间 `O(N²C)`，空间 `O(NC)`。
## 边界条件与本地验证
覆盖单元素及非子集列表。
