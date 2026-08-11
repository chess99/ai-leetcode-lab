# 515. 在每个树行中找最大值

- 难度：MEDIUM
- 标签：树, 深度优先搜索, 广度优先搜索, 二叉树
- 来源：https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
- 归档：2026-08-11T17:13:09Z

## 题目

<p>给定一棵二叉树的根节点&nbsp;<code>root</code> ，请找出该二叉树中每一层的最大值。</p>

<p>&nbsp;</p>

<p><strong>示例1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg" style="height: 172px; width: 300px;" /></p>

<pre>
<strong>输入: </strong>root = [1,3,2,5,3,null,9]
<strong>输出: </strong>[1,3,9]
</pre>

<p><strong>示例2：</strong></p>

<pre>
<strong>输入: </strong>root = [1,2,3]
<strong>输出: </strong>[1,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>二叉树的节点个数的范围是 <code>[0,10<sup>4</sup>]</code></li>
	<li><meta charset="UTF-8" /><code>-2<sup>31</sup>&nbsp;&lt;= Node.val &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p>&nbsp;</p>


## 样例输入

```text
[1,3,2,5,3,null,9]
```
