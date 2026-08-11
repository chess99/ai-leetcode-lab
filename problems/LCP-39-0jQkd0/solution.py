# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:27:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        counts = {}
        for row in source:
            for color in row:
                counts[color] = counts.get(color, 0) + 1

        switches = 0
        for row in target:
            for color in row:
                if counts.get(color, 0):
                    counts[color] -= 1
                else:
                    switches += 1
        return switches
