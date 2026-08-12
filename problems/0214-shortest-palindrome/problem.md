# 214. 最短回文串

- 难度：HARD
- 标签：字符串, 字符串匹配, Manacher 算法, 哈希函数, 滚动哈希, KMP 算法, 扩展 KMP
- 来源：https://leetcode.cn/problems/shortest-palindrome/
- 归档：2026-08-12T05:38:09Z

## 题目

<p>给定一个字符串 <em><strong>s</strong></em>，你可以通过在字符串前面添加字符将其转换为<span data-keyword="palindrome-string">回文串</span>。找到并返回可以用这种方式转换的最短回文串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aacecaaa"
<strong>输出：</strong>"aaacecaaa"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd"
<strong>输出：</strong>"dcbabcd"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 样例输入

```text
"aacecaaa"
```
