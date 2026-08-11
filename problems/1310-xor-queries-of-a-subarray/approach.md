# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

建立异或前缀和，区间 `[l,r]` 的异或为 `prefix[r+1] ^ prefix[l]`。

## 复杂度

预处理 `O(n)`，每次查询 `O(1)`，空间 `O(n)`。

## 边界条件与本地验证

- 单元素区间同样适用。
- 本地验证了题目示例和多个重叠查询。
