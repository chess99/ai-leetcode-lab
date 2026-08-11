# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:30:08Z
# Experiment: ai-leetcode-lab, round 1
from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        values = [str(num) for num in nums]

        def compare(left: str, right: str) -> int:
            if left + right > right + left:
                return -1
            if left + right < right + left:
                return 1
            return 0

        result = "".join(sorted(values, key=cmp_to_key(compare)))
        return "0" if result[0] == "0" else result
