# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

用埃氏筛标记至 `right` 的质数，再线性扫描区间，比较相邻质数差并维护最小对。

## 复杂度

筛法时间 `O(right log log right)`，空间 `O(right)`。

## 边界条件与本地验证

0 和 1 显式标为非质数；区间中不足两个质数返回 `[-1,-1]`。已验证题面样例及无质数对区间。
