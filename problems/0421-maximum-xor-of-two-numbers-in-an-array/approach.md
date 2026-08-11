# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
从高位到低位贪心尝试将答案位设为 1，保存当前位掩码下的所有前缀并检查是否存在可配对前缀。
## 复杂度
时间 `O(32n)`，空间 `O(n)`。
## 边界条件与本地验证
单元素返回 0。已断言样例并通过 `py_compile`。
