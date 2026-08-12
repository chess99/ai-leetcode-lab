# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

按长度排序，每词删除一个字符生成前驱，哈希 DP 取最长前驱加一。

## 复杂度

时间 `O(总字符数²)`，空间 `O(词数)`。

## 边界条件与本地验证

- 完成 `py_compile` 和链/单词断言。
