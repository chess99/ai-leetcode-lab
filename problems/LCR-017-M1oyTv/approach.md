# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

滑动窗口维护目标字符欠缺数；窗口覆盖目标时不断收缩并记录最短区间。

## 复杂度

`O(|s|+|t|)` 时间，`O(|字符集|)` 空间。

## 边界条件与本地验证

三个题面样例输出 `BANC`、`a`、空串。
