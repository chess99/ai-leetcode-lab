# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

对子树同时维护总工作量 `work` 与两核完成该子树的最短时间 `time`。左右前导子树之间无依赖且任务可抢占，因此合并它们所需时间为 `max(leftTime,rightTime,(leftWork+rightWork)/2)`；两个子树完成后，当前节点只能由一个核执行，再串行加 `node.val`。

## 复杂度

每个节点访问一次，时间 `O(n)`；递归栈空间 `O(h)`。

## 边界条件与本地验证

空子树工作量和时间均为 0；结果可能是半整数。本地验证三个样例，并对小树的工作量下界与链、星形边界进行核对。
