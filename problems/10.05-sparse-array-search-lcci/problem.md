# 面试题 10.05. 稀疏数组搜索

- 难度：EASY
- 标签：数组, 字符串, 二分查找
- 来源：https://leetcode.cn/problems/sparse-array-search-lcci/
- 归档：2026-08-11T15:59:37Z

## 题目

<p>稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入：</strong>words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
<strong> 输出：</strong>-1
<strong> 说明：</strong>不存在返回-1。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
<strong> 输出</strong>：4
</pre>

<p><strong>提示:</strong></p>

<ol>
	<li>words的长度在[1, 1000000]之间</li>
</ol>


## 样例输入

```text
["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
"ta"
```
