# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

偶数下标字符只能互换，奇数下标字符只能互换，分别排序两组作为等价类签名。

## 复杂度

时间 O(总长度 log 长度)，空间 O(总长度)。

## 边界条件与本地验证

奇偶位置不能混合；本地对示例断言并执行 py_compile。
