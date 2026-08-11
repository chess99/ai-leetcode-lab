# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:41:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for char in s:
            if len(result) < 2 or char != result[-1] or char != result[-2]:
                result.append(char)
        return "".join(result)
