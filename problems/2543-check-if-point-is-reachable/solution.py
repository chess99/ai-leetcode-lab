# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:32Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd


class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        common = gcd(targetX, targetY)
        return common & (common - 1) == 0
