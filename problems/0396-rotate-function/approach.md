# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
先计算 F(0) 和数组和，使用递推 `F(k)=F(k-1)+sum-n*移入首位元素` 线性更新最大值。
## 复杂度
时间 `O(n)`，空间 `O(1)`。
## 边界条件与本地验证
单元素保持原值。已断言样例并通过 `py_compile`。
