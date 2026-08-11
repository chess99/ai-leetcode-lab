# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for ch in str1:
            if j < len(str2) and (ch == str2[j] or chr((ord(ch)-97+1)%26+97) == str2[j]): j += 1
        return j == len(str2)
