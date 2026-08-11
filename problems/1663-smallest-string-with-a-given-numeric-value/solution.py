# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ['a'] * n; extra = k - n
        for index in range(n - 1, -1, -1):
            add = min(25, extra); result[index] = chr(ord('a') + add); extra -= add
        return ''.join(result)
