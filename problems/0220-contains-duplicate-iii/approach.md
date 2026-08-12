# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

按 valueDiff+1 宽度分桶，窗口内同桶或相邻桶满足差距条件即可返回真。

## 复杂度

时间 O(n)，空间 O(indexDiff)。

## 边界条件与本地验证

Python 整除正确覆盖负值；过期元素按下标删除。
