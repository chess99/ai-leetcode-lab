# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:34:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for char in magazine:
            counts[char] = counts.get(char, 0) + 1
        for char in ransomNote:
            if counts.get(char, 0) == 0:
                return False
            counts[char] -= 1
        return True
