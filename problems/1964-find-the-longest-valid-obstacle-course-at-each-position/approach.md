# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

维护非递减子序列各长度的最小结尾；使用 upper_bound 允许相等高度延长。

## 复杂度

时间 O(n log n)，空间 O(n)。

## 边界条件与本地验证

相同高度必须可接；小数组枚举所有子序列核对。
