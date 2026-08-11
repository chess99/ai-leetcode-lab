# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:06Z
# Experiment: ai-leetcode-lab, round 1
from math import isqrt
from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        students = len(grades)
        return (isqrt(8 * students + 1) - 1) // 2
