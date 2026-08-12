# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
数位 DP 统计不超过上界且数位和在范围内的数，两个上界结果相减。
## 复杂度
时间 O(位数·maxSum·10)，空间 O(位数·maxSum)。
## 边界条件与本地验证
下界为一时前缀上界为零；小范围逐个求数位和核对。
