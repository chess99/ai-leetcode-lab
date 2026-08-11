# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:24:39Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        needed = Counter(s1)
        window = Counter(s2[:len(s1)])
        if window == needed:
            return True
        for right in range(len(s1), len(s2)):
            window[s2[right]] += 1
            left_char = s2[right - len(s1)]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if window == needed:
                return True
        return False
