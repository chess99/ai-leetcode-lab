# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total = duration
        for index in range(1, len(timeSeries)):
            total += min(duration, timeSeries[index] - timeSeries[index - 1])
        return total
