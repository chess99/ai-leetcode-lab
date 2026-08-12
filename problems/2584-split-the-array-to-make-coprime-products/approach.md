# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
记录每个质因子的最右位置，扫描左段维护必须覆盖的最远位置。
## 复杂度
时间 O(n√V)，空间 O(质因子数)。
## 边界条件与本地验证
末位不能切分；逐切点求两侧乘积公约数核对。
