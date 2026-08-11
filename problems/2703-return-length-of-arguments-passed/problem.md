# 2703. 返回传递的参数的长度

- 难度：EASY
- 标签：无
- 来源：https://leetcode.cn/problems/return-length-of-arguments-passed/
- 归档：2026-08-11T14:12:23Z

## 题目

请你编写一个函数 <code>argumentsLength</code>，返回传递给该函数的参数数量。
<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>args = [5]
<b>输出：</b>1
<strong>解释：</strong>
argumentsLength(5); // 1

只传递了一个值给函数，因此它应返回 1。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>args = [{}, null, "3"]
<b>输出：</b>3
<b>解释：</b>
argumentsLength({}, null, "3"); // 3

传递了三个值给函数，因此它应返回 3。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>args</code>&nbsp;是一个有效的 JSON 数组</li>
	<li><code>0 &lt;= args.length &lt;= 100</code></li>
</ul>


## 样例输入

```text
[5]
```
