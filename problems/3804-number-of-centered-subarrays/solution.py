# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        nexorviant = nums
        answer = 0
        for left in range(len(nexorviant)):
            total = 0
            values = set()
            for right in range(left, len(nexorviant)):
                total += nexorviant[right]
                values.add(nexorviant[right])
                answer += total in values
        return answer
