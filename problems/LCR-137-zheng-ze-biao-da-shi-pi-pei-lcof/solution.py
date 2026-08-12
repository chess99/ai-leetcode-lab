# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def articleMatch(self, s: str, p: str) -> bool:
        dp = [False] * (len(p) + 1)
        dp[0] = True
        for index in range(2, len(p) + 1):
            if p[index - 1] == '*':
                dp[index] = dp[index - 2]
        for char in s:
            nxt = [False] * (len(p) + 1)
            for index in range(1, len(p) + 1):
                if p[index - 1] == '*':
                    nxt[index] = nxt[index - 2] or (
                        (p[index - 2] == '.' or p[index - 2] == char) and dp[index])
                elif p[index - 1] == '.' or p[index - 1] == char:
                    nxt[index] = dp[index - 1]
            dp = nxt
        return dp[-1]
