# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

排序包裹并做前缀和。对每家供应商排序箱子，二分确定每种箱子覆盖的包裹段并累计浪费。

## 复杂度

时间 O(n log n+总箱子数 log n)，空间 O(n)。

## 边界条件与本地验证

最大箱子不足时跳过该供应商；小输入逐包选择最小可用箱子核对。
