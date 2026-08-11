# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:04:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        first_distance = abs(x - z)
        second_distance = abs(y - z)
        if first_distance == second_distance:
            return 0
        return 1 if first_distance < second_distance else 2
