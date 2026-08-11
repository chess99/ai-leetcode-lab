# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

将数组放入集合，从 k 开始依次检查正倍数，首次不在集合中的倍数就是答案。

## 复杂度

时间复杂度 O(n + q)，q 为检查的倍数数目；额外空间复杂度 O(n)。

## 边界条件与本地验证

只检查正整数倍。已进行 Python 语法检查及最小断言。
