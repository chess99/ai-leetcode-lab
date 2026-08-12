# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

逐个十进制位统计该位为 1 的次数。把数字拆成高位、当前位和低位：当前位为 0、1、大于 1 时分别贡献 `high·factor`、`high·factor+low+1`、`(high+1)·factor`。

## 复杂度

时间 `O(log num)`，空间 `O(1)`。

## 边界条件与本地验证

`num=0` 循环不执行返回 0；所有运算使用整数。本地验证两个样例，并对小范围逐数转字符串计数对拍。
