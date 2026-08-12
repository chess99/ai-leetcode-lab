# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

定位三段首个一并同步比较到末尾，保证三段二进制值相等。

## 复杂度

时间 O(n)，空间 O(1)。

## 边界条件与本地验证

全零可任意分割；一的数量不能被三整除则无解。
