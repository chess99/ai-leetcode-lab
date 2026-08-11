# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:52:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        result = 0
        for size in range(2, num + 1):
            result = (result + target) % size
        return result
