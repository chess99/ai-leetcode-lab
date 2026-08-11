# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
每个 `nums1` 元素与 `nums2` 的首项组成堆；弹出最小对后推入该行下一对。
## 复杂度
时间 `O(k log min(k,m))`，空间 `O(min(k,m))`。
## 边界条件与本地验证
任一数组为空返回空。已做样例断言和 `py_compile`。
