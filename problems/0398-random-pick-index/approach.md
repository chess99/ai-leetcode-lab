# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
水塘抽样使每个目标索引等概率入选。
## 复杂度
- 每次 O(n)，空间 O(1)。
## 边界条件与本地验证
- 目标保证存在；验证返回下标对应目标。
