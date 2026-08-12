# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

把词典单词倒序插入 Trie。从 sentence 的每个结束位置反向沿 Trie 查找，dp[i] 表示前 i 个字符最少未识别数；默认把末字符识别失败，遇到词尾则用对应起点更新。

## 复杂度

时间 O(nL)，L 为词典最长词长；Trie 空间为词典总字符数，dp 空间 O(n)。

## 边界条件与本地验证

空句子返回零；无法匹配任何词时 dp 逐字累加，结果就是句长。
