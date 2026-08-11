# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:08:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(start + duration for start, duration in tasks)
