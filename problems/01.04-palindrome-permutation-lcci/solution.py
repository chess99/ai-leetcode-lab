# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:54:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd = set()
        for char in s:
            if char in odd:
                odd.remove(char)
            else:
                odd.add(char)
        return len(odd) <= 1
