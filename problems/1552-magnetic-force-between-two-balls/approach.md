# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

排序后对最小间距二分；贪心从左到右放置球可验证某间距是否可行。

## 复杂度

时间 `O(n log n + n log range)`，空间 `O(1)`。

## 边界条件与本地验证

仅能放两个球时取两端距离。已用样例验证。
