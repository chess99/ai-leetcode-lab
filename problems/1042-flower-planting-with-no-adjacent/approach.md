# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

逐花园贪心选相邻花园未用的最小颜色；每点度数至多三，四种颜色必足够。

## 复杂度

时间 `O(n+e)`，空间 `O(n+e)`。

## 边界条件与本地验证

- 完成 `py_compile` 和相邻异色断言。
