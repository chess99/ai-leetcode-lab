# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

分别解析等号左右两侧。正则以带可选符号的项为单位提取常数和系数项；x、+x、-x 的系数分别视为 1、1、-1。每一侧都汇总为 coefficient*x + constant。

移项后得到 (left_coefficient-right_coefficient)*x = right_constant-left_constant。系数为零时，常数也为零表示无限解，否则无解；系数非零时按题意保证整除，直接计算 x。

## 复杂度

- 每个字符只参与一次匹配和解析，时间 O(L)，L 为方程长度。
- 除正则匹配结果外只维护常数个整数，工作空间 O(1)。

## 边界条件与本地验证

- 首项可以没有正号，x 的隐式系数必须正确解析。
- 两侧完全相同返回 Infinite solutions。
- 系数抵消但常数不同返回 No solution。

本地对题目三个示例、负解、隐式系数、无限解和无解做最小断言，并执行 py_compile 语法检查。
