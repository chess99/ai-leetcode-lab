# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        all_values = set(); ending = set()
        for value in arr:
            ending = {value | previous for previous in ending} | {value}
            all_values |= ending
        return len(all_values)
