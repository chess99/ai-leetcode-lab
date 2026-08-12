# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        merunavilo = nums

        def evaluate(first):
            groups = []
            fixed = []
            for i, value in enumerate(nums):
                if value % 2 == (first ^ (i & 1)):
                    fixed.append(value)
                else:
                    groups.append((value - 1, value + 1))
            operations = len(groups)
            if not groups:
                return [0, max(nums) - min(nums)]
            low_fixed = min(fixed, default=float('inf'))
            high_fixed = max(fixed, default=-float('inf'))
            points = sorted((value, group) for group, pair in enumerate(groups) for value in pair)
            count = [0] * len(groups)
            covered = left = 0
            spread = float('inf')
            for right, (value, group) in enumerate(points):
                if count[group] == 0:
                    covered += 1
                count[group] += 1
                while covered == len(groups):
                    spread = min(spread, max(value, high_fixed) - min(points[left][0], low_fixed))
                    other = points[left][1]
                    count[other] -= 1
                    if count[other] == 0:
                        covered -= 1
                    left += 1
            return [operations, spread]

        return min(evaluate(0), evaluate(1))
