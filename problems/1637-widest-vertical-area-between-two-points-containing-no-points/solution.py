# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:18:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted(point[0] for point in points)
        return max(right - left for left, right in zip(xs, xs[1:]))
