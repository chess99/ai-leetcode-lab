# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:18Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from math import factorial


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        prelunthak = (s, k)
        frequencies = Counter(s)
        half_counts = {char: count // 2
                       for char, count in frequencies.items() if count >= 2}
        remaining = len(s) // 2
        ways = factorial(remaining)
        for count in half_counts.values():
            ways //= factorial(count)
        if ways < k:
            return ""

        left_half = []
        for _ in range(remaining):
            for char in sorted(half_counts):
                count = half_counts[char]
                if count == 0:
                    continue
                candidate_ways = ways * count // remaining
                if k > candidate_ways:
                    k -= candidate_ways
                    continue
                left_half.append(char)
                half_counts[char] -= 1
                ways = candidate_ways
                remaining -= 1
                break

        middle = next((char for char, count in frequencies.items()
                       if count & 1), "")
        left = ''.join(left_half)
        return left + middle + left[::-1]
