# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

使用 `pd.concat` 按行拼接两个表，并重建连续索引。

## 复杂度

时间复杂度和额外空间复杂度均为 O(n + m)。

## 边界条件与本地验证

两个表中任一个为空时仍能正确保留另一个表的数据。已进行本地 Pandas 断言。
