# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def prime(x: int) -> bool:
            if x < 2: return False
            d = 2
            while d * d <= x:
                if x % d == 0: return False
                d += 1
            return True
        values = set()
        for i in range(len(s)):
            value = 0
            for j in range(i, len(s)):
                value = value * 10 + int(s[j])
                if prime(value): values.add(value)
        return sum(sorted(values, reverse=True)[:3])
