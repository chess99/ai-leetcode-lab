# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
逐次找树路径统计节点经过次数，再做树形独立集 DP 决定哪些非相邻节点半价。
## 复杂度
时间 O(行程数·n+n)，空间 O(n)。
## 边界条件与本地验证
同起终点路径只计一次；小树枚举半价节点集合核对。
