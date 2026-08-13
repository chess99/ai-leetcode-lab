# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:40:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        left, right = 0, len(stock) - 1
        while left < right:
            middle = (left + right) // 2
            if stock[middle] > stock[right]:
                left = middle + 1
            elif stock[middle] < stock[right]:
                right = middle
            else:
                right -= 1
        return stock[left]
