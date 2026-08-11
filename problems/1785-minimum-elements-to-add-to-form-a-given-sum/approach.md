# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

计算与 goal 的绝对差，每个新增元素最多弥补 limit，因此向上除以 limit。

## 正确性

下界由单个元素最大贡献给出；使用若干个 ±limit 和一个余数元素可达到该下界。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

已有和等于目标时返回 0；已用样例验证。
