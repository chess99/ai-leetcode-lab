# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

按 nums1 分组升序扫描，小根堆维护此前严格更小组中最大的 k 个 nums2。

## 复杂度

时间 `O(n log n)`，空间 `O(n)`。

## 边界条件与本地验证

覆盖 nums1 相同元素不得互相贡献。
