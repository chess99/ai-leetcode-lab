# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

对 s、分隔符和反转串求 KMP 前缀函数，末值为最长回文前缀长度，反转剩余后缀前置。

## 复杂度

时间 O(n)，空间 O(n)。

## 边界条件与本地验证

空串和已回文串均直接正确处理。
