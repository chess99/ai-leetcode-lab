# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:40Z
# Experiment: ai-leetcode-lab, round 1
from math import isqrt


class Solution:
    def primePalindrome(self, n: int) -> int:
        for value in (2, 3, 5, 7, 11):
            if n <= value: return value
        def prime(value: int) -> bool:
            for divisor in range(2, isqrt(value) + 1):
                if value % divisor == 0: return False
            return True
        root = 10 ** (len(str(n)) // 2)
        while True:
            text = str(root)
            value = int(text + text[-2::-1])
            if value >= n and prime(value): return value
            root += 1
