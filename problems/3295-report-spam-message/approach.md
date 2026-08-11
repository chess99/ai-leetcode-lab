# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

用集合保存禁词，统计消息中命中禁词的单词数，达到两个即为垃圾信息。

## 复杂度

时间 `O(message.length + bannedWords.length)`，空间 `O(bannedWords.length)`。

## 边界条件与本地验证

覆盖重复禁词命中和仅命中一个禁词。
