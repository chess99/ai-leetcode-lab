# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        if total % len(machines):
            return -1
        average = total // len(machines)
        balance = answer = 0
        for dresses in machines:
            difference = dresses - average
            balance += difference
            answer = max(answer, abs(balance), difference)
        return answer
