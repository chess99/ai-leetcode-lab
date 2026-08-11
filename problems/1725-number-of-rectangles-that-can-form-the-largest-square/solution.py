# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:23:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sides=[min(rectangle) for rectangle in rectangles]; return sides.count(max(sides))
