# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
计数后按频率放桶，从高频桶取前 k 个。
## 复杂度
- 时间 O(n)，空间 O(n)。
## 边界条件与本地验证
- 返回顺序不限。验证 `[1,1,1,2,2,3],2 -> {1,2}`。
