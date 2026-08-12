# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

按精确、忽略大小写、元音归一化优先级建立首次出现映射查询。

## 复杂度

与总字符数成正比。

## 边界条件与本地验证

- 首次单词优先；完成 `py_compile` 和断言。
