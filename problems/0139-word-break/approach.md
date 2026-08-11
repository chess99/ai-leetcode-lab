# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

令 `possible[i]` 表示前 `i` 个字符能否拆分。初始空前缀为真；对每个结束位置，枚举不超过词典最长词长度的起点，若此前缀可拆分且当前切片在词典集合中，则当前位置为真。集合提供平均 O(1) 单词判断。

## 复杂度

- 时间复杂度：O(n·L)，L 为词典中最长单词长度。
- 空间复杂度：O(n + d)，其中 d 为词典集合大小。

## 边界条件与本地验证

- 单词可重复使用，因为状态只记录前缀可达性。
- 无法覆盖最后字符时返回 `False`。
- 验证：`"leetcode", ["leet","code"] -> True`、`"applepenapple", ["apple","pen"] -> True`、`"catsandog", ["cats","dog","sand","and","cat"] -> False`。
