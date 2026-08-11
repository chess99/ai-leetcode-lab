# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:42:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1, -1, -1]
        total = 0
        for index, char in enumerate(s):
            last[ord(char) - ord("a")] = index
            total += min(last) + 1
        return total
