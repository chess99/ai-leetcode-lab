# 131. 分割回文串

- 难度：MEDIUM
- 标签：字符串, 动态规划, 回溯
- 来源：https://leetcode.cn/problems/palindrome-partitioning/
- 归档：2026-08-11T16:24:46Z

## 题目

<p>给你一个字符串 <code>s</code>，请你将<em> </em><code>s</code><em> </em>分割成一些 <span data-keyword="substring-nonempty">子串</span>，使每个子串都是 <strong><span data-keyword="palindrome-string">回文串</span></strong> 。返回 <code>s</code> 所有可能的分割方案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aab"
<strong>输出：</strong>[["a","a","b"],["aa","b"]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "a"
<strong>输出：</strong>[["a"]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 样例输入

```text
"aab"
```
