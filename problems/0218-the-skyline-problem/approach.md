# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

扫描所有边界，堆维护尚未结束建筑的高度，最高高度变化时记录关键点。

## 复杂度

时间 O(n log n)，空间 O(n)。

## 边界条件与本地验证

同一坐标事件逐个处理，最终只保留高度变化点。
