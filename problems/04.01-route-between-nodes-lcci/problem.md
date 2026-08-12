# 面试题 04.01. 节点间通路

- 难度：MEDIUM
- 标签：深度优先搜索, 广度优先搜索, 图
- 来源：https://leetcode.cn/problems/route-between-nodes-lcci/
- 归档：2026-08-12T05:00:50Z

## 题目

<p>节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
<strong> 输出</strong>：true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
<strong> 输出</strong>：true
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li>节点数量n在[0, 1e5]范围内。</li>
	<li>节点编号大于等于 0 小于 n。</li>
	<li>图中可能存在自环和平行边。</li>
</ol>


## 样例输入

```text
3
[[0, 1], [0, 2], [1, 2], [1, 2]]
0
2
```
