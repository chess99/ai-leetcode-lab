# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

从根迭代生成父先于子的遍历序，再逆序计算完成时间。叶子直接取基础时间；非叶子从所有子节点完成时间取最小、最大值，按公式 `2*latest-earliest+baseTime` 计算。

## 复杂度

时间 `O(n)`，空间 `O(n)`。

## 边界条件与本地验证

使用迭代遍历避免深链递归溢出；验证三组样例、单节点和链形树。
