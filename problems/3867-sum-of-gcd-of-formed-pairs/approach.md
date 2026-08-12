# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

按定义扫描前缀最大值并得到每项 gcd；排序后依次把两端配对并累加 gcd。

## 复杂度

时间 O(n log n)，空间 O(n)。

## 边界条件与本地验证

验证奇数长度时中位数未配对。
