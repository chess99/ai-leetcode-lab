# 767. 重构字符串

- 难度：MEDIUM
- 标签：贪心, 哈希表, 字符串, 计数, 排序, 堆（优先队列）
- 来源：https://leetcode.cn/problems/reorganize-string/
- 归档：2026-08-11T17:43:56Z

## 题目

<p>给定一个字符串&nbsp;<code>s</code>&nbsp;，检查是否能重新排布其中的字母，使得两相邻的字符不同。</p>

<p>返回<em> <code>s</code>&nbsp;的任意可能的重新排列。若不可行，返回空字符串&nbsp;<code>""</code></em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> s = "aab"
<strong>输出:</strong> "aba"
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> s = "aaab"
<strong>输出:</strong> ""
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> 只包含小写字母</li>
</ul>


## 样例输入

```text
"aab"
```
