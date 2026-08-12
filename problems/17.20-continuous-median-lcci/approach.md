# 解题记录

- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium；轮次：1

## 思路

用最大堆 lower 保存较小一半（Python 中取相反数），最小堆 upper 保存较大一半。插入后调整到 lower 比 upper 多零个或一个元素。奇数时中位数为 lower 堆顶，偶数时为两堆顶平均值。

## 复杂度

addNum 时间 `O(log N)`，findMedian 时间 `O(1)`，空间 `O(N)`。

## 边界条件与本地验证

覆盖负数、重复数和偶数平均值。官方操作序列依次返回 1.5、2.0。
