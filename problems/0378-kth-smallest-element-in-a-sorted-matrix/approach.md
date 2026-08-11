# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
二分值域，每次从左下角统计不大于中值的元素数。
## 复杂度
- 时间 O(n log range)，空间 O(1)。
## 边界条件与本地验证
- 重复元素按次数计。验证题例 k=8 返回 13。
