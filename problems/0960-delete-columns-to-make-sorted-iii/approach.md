# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

把列视为序列元素，若所有字符串在列 i 到 j 均非降则可连接，求最长合法列子序列。

## 复杂度

时间 O(mn²)，空间 O(n)。

## 边界条件与本地验证

删除数为总列数减最长保留长度。
