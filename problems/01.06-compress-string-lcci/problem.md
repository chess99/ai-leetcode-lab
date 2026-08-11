# 面试题 01.06. 字符串压缩

- 难度：EASY
- 标签：双指针, 字符串
- 来源：https://leetcode.cn/problems/compress-string-lcci/
- 归档：2026-08-11T15:54:53Z

## 题目

<p>字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串<code>aabcccccaaa</code>会变为<code>a2b1c5a3</code>。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>："aabcccccaaa"
<strong>输出</strong>："a2b1c5a3"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入</strong>："abbccd"
<strong>输出</strong>："abbccd"
<strong>解释</strong>："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li>字符串长度在 <code>[0, 50000]</code> 范围内。</li>
</ol>


## 样例输入

```text
"aabcccccaa"
```
