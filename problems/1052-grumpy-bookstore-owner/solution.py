# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:14:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = sum(customer for customer, mood in zip(customers, grumpy) if mood == 0)
        gained = 0
        best_gain = 0
        for index, customer in enumerate(customers):
            if grumpy[index]:
                gained += customer
            if index >= minutes and grumpy[index - minutes]:
                gained -= customers[index - minutes]
            best_gain = max(best_gain, gained)
        return satisfied + best_gain
