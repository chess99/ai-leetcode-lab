# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
离散化后用两个 Fenwick 树统计大于当前值的元素数，按规则放入数组。
## 复杂度
时间 O(n log n)，空间 O(n)。
## 边界条件与本地验证
大于数相等时比较数组长度；按题意直接模拟核对。
