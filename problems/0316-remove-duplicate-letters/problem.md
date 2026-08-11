# 316. 去除重复字母

- 难度：MEDIUM
- 标签：栈, 贪心, 字符串, 单调栈
- 来源：https://leetcode.cn/problems/remove-duplicate-letters/
- 归档：2026-08-11T16:47:13Z

## 题目

<p>给你一个字符串 <code>s</code> ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 <strong>返回结果的<span data-keyword="lexicographically-smaller-string-alien">字典序</span>最小</strong>（要求不能打乱其他字符的相对位置）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong><code>s = "bcabc"</code>
<strong>输出<code>：</code></strong><code>"abc"</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong><code>s = "cbacdcbc"</code>
<strong>输出：</strong><code>"acdb"</code></pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>该题与 1081 <a href="https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters">https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters</a> 相同</p>


## 样例输入

```text
"bcabc"
```
