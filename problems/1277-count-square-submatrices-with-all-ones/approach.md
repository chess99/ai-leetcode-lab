# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
原地 DP：`matrix[r][c]` 记录以该点为右下角的最大全一正方形边长，等于三个邻居最小值加一；累加全部边长。
## 复杂度
时间 `O(MN)`，额外空间 `O(1)`。
## 边界条件与本地验证
覆盖题面两个示例和全零矩阵。
