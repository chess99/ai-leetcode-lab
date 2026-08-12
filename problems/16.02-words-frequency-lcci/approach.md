# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

构造时一次遍历 book，以计数哈希表保存每个单词的频率；get 直接查询。

## 复杂度

构造 O(n)，空间 O(不同单词数)，单次查询平均 O(1)。

## 边界条件与本地验证

哈希计数对不存在的单词返回零，符合题意。
