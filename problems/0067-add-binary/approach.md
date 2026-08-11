# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

从两个字符串末尾开始逐位相加，累加进位。每轮记录当前位，最后反转结果。

## 复杂度

时间 O(max(m, n))，结果数组空间 O(max(m, n))。

## 边界条件与本地验证

覆盖长度不同、连续进位以及最高位产生进位的情况。
