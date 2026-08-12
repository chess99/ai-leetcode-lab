# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

扫描累计数字和符号，遇左括号压入外层和与符号，遇右括号计算内层并合并。

## 复杂度

时间 O(n)，栈空间 O(n)。

## 边界条件与本地验证

支持空格、嵌套括号和一元负号。
