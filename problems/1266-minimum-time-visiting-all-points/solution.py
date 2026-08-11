# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:45:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(x2 - x1), abs(y2 - y1))
                   for (x1, y1), (x2, y2) in zip(points, points[1:]))
