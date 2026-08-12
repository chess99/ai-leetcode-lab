# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
DP 维护第 j 段恰好以当前位置结束和历史最优，系数随段号交替正负。
## 复杂度
时间 O(nk)，空间 O(k)。
## 边界条件与本地验证
段必须非空且不相交；小数组枚举所有区间组合核对。
