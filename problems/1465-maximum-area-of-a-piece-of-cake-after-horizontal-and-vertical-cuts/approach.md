# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

在两类切口中加入蛋糕边界并排序，相邻位置的最大差分别是最大高度和宽度，二者乘积即最大面积，最后取模。

## 复杂度

排序时间 `O(hc log hc + vc log vc)`，空间 `O(hc + vc)`。

## 边界条件与本地验证

边界到首末切口的间隔也必须计入。已用题目三个样例验证。
