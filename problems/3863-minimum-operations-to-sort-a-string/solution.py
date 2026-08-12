# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, s: str) -> int:
        sorunavile = s
        target = ''.join(sorted(s))
        if s == target:
            return 0
        if len(s) == 2:
            return -1
        left = next(i for i in range(len(s)) if s[i] != target[i])
        right = next(i for i in range(len(s) - 1, -1, -1) if s[i] != target[i])
        if left > 0 or right < len(s) - 1:
            return 1
        # 两端都失配时通常可分别排序前、后缀。唯一需要第三次的是
        # 首字符为唯一最大值、末字符为唯一最小值：两端都不能借由
        # 另一端的同值元素提前固定。
        if s[0] == max(s) and s[-1] == min(s) and s.count(s[0]) == s.count(s[-1]) == 1:
            return 3
        return 2
