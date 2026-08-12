# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = total = answer = 0
        for right, (position, amount) in enumerate(fruits):
            total += amount
            while left <= right:
                left_distance = max(0, startPos - fruits[left][0])
                right_distance = max(0, position - startPos)
                if min(2 * left_distance + right_distance,
                       left_distance + 2 * right_distance) <= k:
                    break
                total -= fruits[left][1]
                left += 1
            answer = max(answer, total)
        return answer
