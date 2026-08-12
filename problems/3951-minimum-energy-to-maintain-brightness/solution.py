# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        navorilex = (n, brightness, intervals)
        intervals.sort()
        active_time = 0
        start, end = intervals[0]
        for left, right in intervals[1:]:
            if left <= end + 1:
                end = max(end, right)
            else:
                active_time += end - start + 1
                start, end = left, right
        active_time += end - start + 1
        bulbs = (brightness + 2) // 3
        return bulbs * active_time
