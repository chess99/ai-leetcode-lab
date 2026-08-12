# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

显式未实现。可靠解法仍需按斜率统计平行线段对，同时排除共线四点并正确去重平行四边形；当前实现保留 `NotImplementedError`，避免把未经验证的计数公式误作为答案提交。

## 复杂度

未实现，暂无可声明的最终复杂度。

## 边界条件与本地验证

已确认 Python 文件可加载，调用时明确抛出 `NotImplementedError`，不会静默返回错误结果。
