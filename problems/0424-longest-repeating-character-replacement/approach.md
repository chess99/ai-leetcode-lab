# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
滑动窗口维护窗口最高字符频次；窗口长度减该频次超过 k 时收缩。
## 复杂度
时间 `O(n)`，空间 `O(字符集)`。
## 边界条件与本地验证
`k=0` 退化为连续相同字符。已断言样例并通过 `py_compile`。
