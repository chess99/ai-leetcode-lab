# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
排序后维护以某值结尾的最长连续序列，当前数可保留或加一。
## 复杂度
时间 O(n log n)，空间 O(n)。
## 边界条件与本地验证
重复值的两个选择要分别更新；小数组枚举修改选择核对。
