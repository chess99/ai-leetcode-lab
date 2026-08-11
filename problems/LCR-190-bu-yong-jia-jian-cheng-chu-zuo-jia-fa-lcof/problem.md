# LCR 190. 加密运算

- 难度：EASY
- 标签：位运算, 数学
- 来源：https://leetcode.cn/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/
- 归档：2026-08-11T15:52:28Z

## 题目

<p>计算机安全专家正在开发一款高度安全的加密通信软件，需要在进行数据传输时对数据进行加密和解密操作。假定 <code>dataA</code> 和 <code>dataB</code> 分别为随机抽样的两次通信的数据量：</p>

<ul>
	<li>正数为发送量</li>
	<li>负数为接受量</li>
	<li>0 为数据遗失</li>
</ul>

<p>请不使用四则运算符的情况下实现一个函数计算两次通信的数据量之和（三种情况均需被统计），以确保在数据传输过程中的高安全性和保密性。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>dataA = 5, dataB = -1
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>dataA</code>&nbsp;和 <code>dataB</code>&nbsp;均可能是负数或 0</li>
	<li>结果不会溢出 32 位整数</li>
</ul>

<p>&nbsp;</p>


## 样例输入

```text
5
-1
```
