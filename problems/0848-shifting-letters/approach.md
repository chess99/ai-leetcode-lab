# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

从右向左累积后缀位移并模 26，每个字符只应用该后缀总位移。

## 复杂度

时间 O(n)，空间 O(n)。

## 边界条件与本地验证

大位移取模；z 可回绕到 a。本地对示例和回绕断言，并执行 py_compile。
