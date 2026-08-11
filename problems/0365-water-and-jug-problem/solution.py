# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:18Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        return target <= x + y and (target == 0 or target % gcd(x, y) == 0)
