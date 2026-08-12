# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

按字符计数回溯，每选择一个可用字符即形成一个新序列并继续扩展。

## 复杂度

与不同排列数成正比。

## 边界条件与本地验证

- 重复字符由计数去重；完成 `py_compile` 和断言。
