# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
频次少于 k 的字符不可能出现在答案中，以它分割字符串并递归求各段最大值。
## 复杂度
最坏 `O(n^2)`，递归与切分占额外空间。
## 边界条件与本地验证
长度小于 k 返回 0。已断言样例并通过 `py_compile`。
