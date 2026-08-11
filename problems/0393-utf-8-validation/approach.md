# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
逐字节识别首字节并记录所需续字节数，续字节必须以 `10` 开头。
## 复杂度
时间 `O(n)`，空间 `O(1)`。
## 边界条件与本地验证
末尾不能遗留续字节需求。已做有效、无效字节断言和 `py_compile`。
