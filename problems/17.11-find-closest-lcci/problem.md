# 面试题 17.11. 单词距离

- 难度：MEDIUM
- 标签：数组, 字符串
- 来源：https://leetcode.cn/problems/find-closest-lcci/
- 归档：2026-08-12T05:22:48Z

## 题目

<p>有个内含单词的超大文本文件，给定任意两个<code>不同的</code>单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
<strong>输出：</strong>1</pre>

<p>提示：</p>

<ul>
	<li><code>words.length &lt;= 100000</code></li>
</ul>


## 样例输入

```text
["I","am","a","student","from","a","university","in","a","city"]
"a"
"student"
```
