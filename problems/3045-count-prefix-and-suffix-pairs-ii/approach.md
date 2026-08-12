# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
把单词每层首尾字符组成配对 Trie，沿当前词路径累计此前完整单词数。
## 复杂度
时间 O(总字符数)，空间 O(总字符数)。
## 边界条件与本地验证
相同单词形成配对；随机词表与双循环核对。
