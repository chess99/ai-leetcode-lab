# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

逐药水计算最早开始时间，使其经过每位巫师时不早于该巫师上瓶完成时间。

## 复杂度

时间 `O(nm)`，空间 `O(n)`。

## 边界条件与本地验证

覆盖所有技能相同和题面示例。
