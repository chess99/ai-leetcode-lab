# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

逐个检查 `words` 中的字符串是否为 `s` 的前缀。Python 的 `str.startswith` 直接表达这一条件；布尔值可作为 `0/1` 求和得到答案。

## 复杂度

设所有被比较前缀的长度之和为 L，时间复杂度为 O(L)，额外空间复杂度为 O(1)。

## 边界条件与本地验证

覆盖只有一个单词、所有单词都是前缀、没有单词是前缀，以及单词比 `s` 更长的情况；后一种情况会由 `startswith` 正确返回假。
