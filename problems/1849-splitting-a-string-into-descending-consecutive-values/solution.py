# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index, previous):
            if index == len(s): return True
            value = 0
            for end in range(index, len(s)):
                value = value * 10 + int(s[end])
                if value == previous - 1 and dfs(end + 1, value): return True
                if value >= previous: return False
            return False
        return any(dfs(end + 1, int(s[:end + 1])) for end in range(len(s) - 1))
