# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:29:06Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        remaining, need = Counter(nums), Counter()
        for number in nums:
            if remaining[number] == 0: continue
            remaining[number] -= 1
            if need[number]:
                need[number] -= 1; need[number + 1] += 1
            elif remaining[number + 1] and remaining[number + 2]:
                remaining[number + 1] -= 1; remaining[number + 2] -= 1; need[number + 3] += 1
            else: return False
        return True
