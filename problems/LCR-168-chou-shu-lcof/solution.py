# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        index2 = index3 = index5 = 0
        for index in range(1, n):
            next_value = min(ugly[index2] * 2,
                             ugly[index3] * 3,
                             ugly[index5] * 5)
            ugly[index] = next_value
            while ugly[index2] * 2 <= next_value:
                index2 += 1
            while ugly[index3] * 3 <= next_value:
                index3 += 1
            while ugly[index5] * 5 <= next_value:
                index5 += 1
        return ugly[-1]
