# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
栈保存进入括号前字符串和重复次数；遇到右括号拼接展开内容。
## 复杂度
时间与输出长度线性相关，空间为嵌套深度和输出。
## 边界条件与本地验证
支持多位数字和嵌套。已断言样例并通过 `py_compile`。
