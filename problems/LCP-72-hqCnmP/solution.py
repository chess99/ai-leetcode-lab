# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:32:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        target = len(supplies) // 2
        while len(supplies) > target:
            index = min(range(len(supplies) - 1), key=lambda i: supplies[i] + supplies[i + 1])
            supplies[index : index + 2] = [supplies[index] + supplies[index + 1]]
        return supplies
