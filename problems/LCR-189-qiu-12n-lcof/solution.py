# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:45Z
# Experiment: ai-leetcode-lab, round 1
import sys


sys.setrecursionlimit(20000)


class Solution:
    def mechanicalAccumulator(self, target: int) -> int:
        return target and target + self.mechanicalAccumulator(target - 1)
