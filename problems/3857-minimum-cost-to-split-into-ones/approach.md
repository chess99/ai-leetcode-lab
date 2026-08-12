# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

一次把 x 拆成 a、b 的代价 ab，且 x²=a²+b²+2ab。对整棵拆分树求和，内部平方项望远镜消去，总代价恒为 (n²-n)/2。

## 复杂度

时间 O(1)，空间 O(1)。

## 边界条件与本地验证

验证 n=1、3、4 及递推小规模枚举。
