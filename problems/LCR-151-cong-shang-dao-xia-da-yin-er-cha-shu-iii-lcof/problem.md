# LCR 151. 彩灯装饰记录 III

- 难度：MEDIUM
- 标签：树, 广度优先搜索, 二叉树
- 来源：https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
- 归档：2026-08-12T04:46:34Z

## 题目

<p>一棵圣诞树记作根节点为 <code>root</code> 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照如下规则记录彩灯装饰结果：</p>

<ul>
	<li>第一层按照从左到右的顺序记录</li>
	<li>除第一层外每一层的记录顺序均与上一层相反。即第一层为从左到右，第二层为从右到左。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1694758674-XYrUiV-%E5%89%91%E6%8C%87%20Offer%2032%20-%20I_%E7%A4%BA%E4%BE%8B1.png" /></p>

<pre>
<strong>输入：</strong>root = [8,17,21,18,null,null,6]
<strong>输出：</strong>[[8],[21,17],[18,6]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>节点总数 &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>


## 样例输入

```text
[8,17,21,18,null,null,6]
```
