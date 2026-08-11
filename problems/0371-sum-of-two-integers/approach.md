# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
异或计算无进位和，按位与左移计算进位，在 32 位掩码下迭代至无进位。
## 复杂度
时间 `O(1)`，空间 `O(1)`。
## 边界条件与本地验证
最后将无符号结果恢复为有符号值。已做正负数断言和 `py_compile`。
