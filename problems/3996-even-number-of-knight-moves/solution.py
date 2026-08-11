# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:24:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return (start[0]+start[1])%2 == (target[0]+target[1])%2
