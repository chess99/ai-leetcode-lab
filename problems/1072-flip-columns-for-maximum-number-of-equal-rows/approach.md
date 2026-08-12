# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

将每行按首位归一化（首位为一时整行取反），相同模式可同时变为全零或全一。

## 复杂度

时间 `O(mn)`，空间 `O(mn)`。

## 边界条件与本地验证

- 完成 `py_compile` 和断言。
