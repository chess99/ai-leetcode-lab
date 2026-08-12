# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

k 为一时只能形成循环旋转，枚举取最小；k 大于一时可通过操作实现任意排列，直接排序。

## 复杂度

时间 O(n²)（k=1）或 O(n log n)，空间 O(n)。

## 边界条件与本地验证

单字符和重复字符均适用。
