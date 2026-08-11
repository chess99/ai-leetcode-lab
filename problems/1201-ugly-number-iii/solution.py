# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:28:40Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(first, second):
            return first // gcd(first, second) * second
        ab, ac, bc = lcm(a, b), lcm(a, c), lcm(b, c)
        abc = lcm(ab, c)
        def count(value):
            return value // a + value // b + value // c - value // ab - value // ac - value // bc + value // abc
        left, right = 1, 2 * 10 ** 9
        while left < right:
            middle = (left + right) // 2
            if count(middle) >= n: right = middle
            else: left = middle + 1
        return left
