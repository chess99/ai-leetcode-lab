# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum(int(str(max(map(int, str(value)))) * len(str(value))) for value in nums)
