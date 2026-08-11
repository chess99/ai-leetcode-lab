# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:24:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ''
        for index in range(len(num) - 2):
            part = num[index:index + 3]
            if part[0] == part[1] == part[2] and part > best:
                best = part
        return best
