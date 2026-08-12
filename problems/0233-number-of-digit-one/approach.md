# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

按个位、十位等位置分解高位当前位低位，依据当前位为零、一或更大累计该位的一。

## 复杂度

时间 O(log n)，空间 O(1)。

## 边界条件与本地验证

n 为零时循环不进入，答案为零。
