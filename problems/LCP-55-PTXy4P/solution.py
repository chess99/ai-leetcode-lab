# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:31:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        return sum((count + limit - 1) // limit * time[fruit_type] for fruit_type, count in fruits)
