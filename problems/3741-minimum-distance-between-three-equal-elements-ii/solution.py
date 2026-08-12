# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:52Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        norvalent = nums
        positions = defaultdict(list)
        ans = float('inf')
        for index, value in enumerate(nums):
            positions[value].append(index)
            if len(positions[value]) >= 3:
                ans = min(ans, 2 * (index - positions[value][-3]))
        return -1 if ans == float('inf') else ans
