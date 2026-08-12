# 面试题 17.18. 最短超串

- 难度：MEDIUM
- 标签：数组, 哈希表, 滑动窗口
- 来源：https://leetcode.cn/problems/shortest-supersequence-lcci/
- 归档：2026-08-12T05:22:47Z

## 题目

<p>假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。</p>

<p>返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
big = <code>[7,5,9,0,2,1,3,<strong>5,7,9,1</strong>,1,5,8,8,9,7]
small = [1,5,9]</code>
<strong>输出：</strong>[7,10]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>
big = <code>[1,2,3]
small = [4]</code>
<strong>输出：</strong>[]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>big.length&nbsp;&lt;= 100000</code></li>
	<li><code>1 &lt;= small.length&nbsp;&lt;= 100000</code></li>
</ul>


## 样例输入

```text
[7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
[1, 5, 9]
```
