# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:05:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        start = 0
        for index in range(1, len(s) + 1):
            if index == len(s) or s[index] != s[start]:
                if index - start >= 3:
                    result.append([start, index - 1])
                start = index
        return result
