# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

从右上角开始：值过大则左移，值过小则下移；每步排除一整列或一整行。

## 复杂度

时间 `O(m+n)`，空间 `O(1)`。

## 边界条件与本地验证

- 空矩阵返回假。

本地断言示例命中与未命中及空矩阵，并通过 `py_compile`。
