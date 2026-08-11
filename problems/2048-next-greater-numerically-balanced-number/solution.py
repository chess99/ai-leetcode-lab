# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:18Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        candidate = n + 1
        while True:
            frequency = Counter(str(candidate))
            if all(int(digit) == count for digit, count in frequency.items()):
                return candidate
            candidate += 1
