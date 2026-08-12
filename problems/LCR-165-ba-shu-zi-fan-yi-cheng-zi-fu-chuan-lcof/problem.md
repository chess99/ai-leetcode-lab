# LCR 165. 解密数字

- 难度：MEDIUM
- 标签：字符串, 动态规划
- 来源：https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
- 归档：2026-08-12T05:00:42Z

## 题目

<p>现有一串神秘的密文 <code>ciphertext</code>，经调查，密文的特点和规则如下：</p>

<ul>
	<li>密文由非负整数组成</li>
	<li>数字 0-25 分别对应字母 a-z</li>
</ul>

<p>请根据上述规则将密文 <code>ciphertext</code> 解密为字母，并返回共有多少种解密结果。</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>ciphertext = 216612
<strong>输出：</strong><code>6
</code><strong>解释：</strong>216612 解密后有 6 种不同的形式，分别是 "cbggbc"，"vggbc"，"vggm"，"cbggm"，"cqgbc" 和 "cqgm" </pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= ciphertext &lt; 2<sup>31</sup></code></li>
</ul>

<p>&nbsp;</p>


## 样例输入

```text
216612
```
