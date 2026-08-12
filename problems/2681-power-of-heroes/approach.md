# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
排序后把当前数作为最大值，前缀累积其作为较小元素的最小值贡献。
## 复杂度
时间 O(n log n)，空间 O(1)。
## 边界条件与本地验证
单元素直接计立方；枚举子集最小最大值核对。
