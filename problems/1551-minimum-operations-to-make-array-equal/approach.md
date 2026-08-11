# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

两端元素向平均值靠拢，所需操作数形成等差和，化简为 `n*n//4`。

## 复杂度

时间和空间均为 `O(1)`。

## 边界条件与本地验证

奇偶 n 均适用。已用小 n 验证。
