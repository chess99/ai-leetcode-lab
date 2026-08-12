# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

把单词插入 Trie，从每格 DFS 沿前缀搜索，命中词尾即记录并删除标记去重。

## 复杂度

搜索最坏与网格和词长相关，Trie 空间为词长总和。

## 边界条件与本地验证

回溯时恢复格子，避免一个单词重复使用格子。
