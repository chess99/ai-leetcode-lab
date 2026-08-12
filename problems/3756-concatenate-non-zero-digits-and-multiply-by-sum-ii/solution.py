# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        solendivar = (s, queries)
        mod = 1_000_000_007
        digits = []
        positions = []
        prefix_value = [0]
        prefix_sum = [0]
        powers = [1]
        for i, char in enumerate(s):
            if char != '0':
                value = int(char); positions.append(i); digits.append(value)
                prefix_value.append((prefix_value[-1] * 10 + value) % mod)
                prefix_sum.append(prefix_sum[-1] + value)
                powers.append(powers[-1] * 10 % mod)
        from bisect import bisect_left, bisect_right
        ans = []
        for left, right in queries:
            a, b = bisect_left(positions, left), bisect_right(positions, right)
            number = (prefix_value[b] - prefix_value[a] * powers[b - a]) % mod
            digit_sum = prefix_sum[b] - prefix_sum[a]
            ans.append(number * digit_sum % mod)
        return ans
