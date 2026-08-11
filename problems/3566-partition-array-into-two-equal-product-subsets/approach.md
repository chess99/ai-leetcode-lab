# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

枚举第一个子集的位掩码，计算其和补集的乘积，二者都等于 target 即成功。

## 复杂度

时间 O(n·2^n)，空间 O(1)（不计输入）；n 至多 12，可直接枚举。

## 边界条件与本地验证

待填写。
