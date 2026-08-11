# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

将二维列表传给 `DataFrame` 构造函数，并显式指定两列列名。

## 复杂度

时间复杂度和额外空间复杂度均为 O(n)。

## 边界条件与本地验证

输入顺序会保留，空列表也会得到包含正确列名的空表。已进行本地 Pandas 断言。
