# 解题记录

- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium；轮次：1

## 思路

令 `adjusted[i] = nums[i] - i`，把前缀变成递增 1 的数组，等价于把 adjusted 前缀全部改成同一个数。绝对值和在中位数处最小。用两个堆维护中位数及两侧元素和，即可在每次插入后常数时间计算代价。

## 复杂度

时间 `O(N log N)`，空间 `O(N)`。

## 边界条件与本地验证

三个官方样例全部通过；随机数组与排序取中位数的 `O(N² log N)` oracle 对拍通过。
