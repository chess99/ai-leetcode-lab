# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:43:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutations = [""]
        for char in s:
            if char.isalpha():
                permutations = [prefix + variant for prefix in permutations for variant in (char.lower(), char.upper())]
            else:
                permutations = [prefix + char for prefix in permutations]
        return permutations
