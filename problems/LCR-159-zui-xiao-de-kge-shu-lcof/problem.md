# LCR 159. 库存管理 III

- 难度：EASY
- 标签：数组, 分治, 快速选择, 排序, 堆（优先队列）
- 来源：https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/
- 归档：2026-08-11T15:43:24Z

## 题目

<p>仓库管理员以数组 <code>stock</code> 形式记录商品库存表，其中 <code>stock[i]</code> 表示对应商品库存余量。请返回库存余量最少的 <code>cnt</code> 个商品余量，返回&nbsp;<strong>顺序不限</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>stock = [2,5,7,4], cnt = 1
<strong>输出：</strong>[2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>stock = [0,2,3,6], cnt = 2
<strong>输出：</strong>[0,2] 或 [2,0]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= cnt &lt;= stock.length &lt;= 10000</code></li>
	<li><code>0 &lt;= stock[i] &lt;= 10000</code></li>
</ul>

<p>&nbsp;</p>


## 样例输入

```text
[2,5,7,4]
1
```
