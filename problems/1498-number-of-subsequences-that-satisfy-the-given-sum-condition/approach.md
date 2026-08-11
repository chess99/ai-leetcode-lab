# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
排序后双指针。最小值与最大值合法时，中间元素任取，共 `2^(r-l)` 种。
## 复杂度
时间 `O(N log N)`，空间 `O(N)`。
## 边界条件与本地验证
覆盖无合法子序列和单元素子序列。
