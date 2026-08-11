# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

从 Customers 选取客户名，并用 NOT EXISTS 判断 Orders 中是否不存在 customerId 与该客户 id 相等的订单。

## 复杂度

时间复杂度 O(C + O)，空间复杂度 O(1)（建立 customerId 索引或优化器可使用半连接）。

## 边界条件与本地验证

客户有任意数量订单都会被排除；Orders 为空时所有客户都返回；不存在订单的客户正常保留。
