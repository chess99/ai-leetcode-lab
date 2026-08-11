# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
路径位掩码记录数字奇偶，叶节点至多一位置位即可重排成回文。
## 复杂度
时间 `O(N)`，空间 `O(H)`。
## 边界条件与本地验证
覆盖单节点和多个奇数频次路径。
