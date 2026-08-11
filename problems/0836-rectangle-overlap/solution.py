# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:05:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return (max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]) and
                max(rec1[1], rec2[1]) < min(rec1[3], rec2[3]))
