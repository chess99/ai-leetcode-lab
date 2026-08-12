# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:48Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        waiting = defaultdict(int)
        answer = []
        for value in nums:
            complement = target - value
            if waiting[complement]:
                waiting[complement] -= 1
                answer.append([complement, value])
            else:
                waiting[value] += 1
        return answer
