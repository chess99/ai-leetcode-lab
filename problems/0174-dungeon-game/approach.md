# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

从终点逆推 dp，表示进入该格所需最低生命值，只能向右或下取较小需求。

## 复杂度

时间 O(mn)，滚动数组空间 O(n)。

## 边界条件与本地验证

最低生命始终至少为一。
