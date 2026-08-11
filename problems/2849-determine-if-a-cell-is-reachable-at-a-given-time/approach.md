# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
八方向移动最短步数为切比雪夫距离；仅起终点相同且 t=1 无法原地停留。
## 复杂度
时间和空间均为 `O(1)`。
## 边界条件与本地验证
处理特殊 t=1；已验证样例。
