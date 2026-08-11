# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:10Z
# Experiment: ai-leetcode-lab, round 1

from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        counts = Counter(num)
        left = []

        for digit in range(9, -1, -1):
            char = str(digit)
            if digit == 0 and not left:
                continue
            pairs = counts[char] // 2
            if pairs:
                left.append(char * pairs)

        half = ''.join(left)
        middle = next((str(digit) for digit in range(9, -1, -1) if counts[str(digit)] % 2), '')
        if not half:
            return middle or '0'
        return half + middle + half[::-1]
