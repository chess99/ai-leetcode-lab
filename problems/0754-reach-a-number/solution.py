# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        steps = 0
        distance = 0
        while distance < target or (distance - target) % 2:
            steps += 1
            distance += steps
        return steps
