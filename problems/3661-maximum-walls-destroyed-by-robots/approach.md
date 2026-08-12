# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

显式未实现。机器人射击区间会被相邻机器人位置截断，左右射击之间还存在覆盖冲突；当前未得到经过 oracle 验证的区间 DP 状态，因此保留 `NotImplementedError`。

## 复杂度

未实现，暂无可声明的最终复杂度。

## 边界条件与本地验证

已补齐类型导入并确认模块可加载；函数调用会明确抛错，避免误提交不可靠的贪心。
