# 面试题 17.22. 单词转换

- 难度：MEDIUM
- 标签：广度优先搜索, 哈希表, 字符串, 回溯
- 来源：https://leetcode.cn/problems/word-transformer-lcci/
- 归档：2026-08-12T05:22:47Z

## 题目

<p>给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。</p>

<p>编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

<strong>输出：</strong>
["hit","hot","dot","lot","log","cog"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

<strong>输出：</strong>[]

<strong>解释：</strong><em>endWord</em> "cog" 不在字典中，所以不存在符合要求的转换序列。</pre>


## 样例输入

```text
"hit"
"cog"
["hot","dot","dog","lot","log","cog"]
```
