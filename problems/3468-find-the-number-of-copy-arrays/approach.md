# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

所有元素由首元素和固定差分决定；将每行边界反推到首元素并取交集。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

覆盖交集为空和单元素数组。
