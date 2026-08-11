# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
树状数组保存前缀增量，更新和区间和均转为 O(log n) 操作。
## 复杂度
- 构建 O(n log n)，更新/查询 O(log n)，空间 O(n)。
## 边界条件与本地验证
- 使用 1 基下标。验证 `[1,3,5]` 查询 9、更新后查询 8。
