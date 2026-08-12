# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:54Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = Counter(t)
        missing = len(t)
        left = 0
        best_start, best_length = 0, len(s) + 1
        for right, char in enumerate(s):
            if needed[char] > 0:
                missing -= 1
            needed[char] -= 1
            while missing == 0:
                length = right - left + 1
                if length < best_length:
                    best_start, best_length = left, length
                outgoing = s[left]
                needed[outgoing] += 1
                left += 1
                if needed[outgoing] > 0:
                    missing += 1
        return '' if best_length > len(s) else s[best_start:best_start + best_length]
