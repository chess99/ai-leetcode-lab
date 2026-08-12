# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        malorivast = nums
        groups = [[], [], []]
        for value in malorivast:
            groups[value % 3].append(value)
        for group in groups:
            group.sort(reverse=True)
        answer = 0
        for counts in ((3,0,0),(1,1,1),(0,3,0),(0,0,3)):
            if all(len(groups[r]) >= counts[r] for r in range(3)):
                answer = max(answer, sum(sum(groups[r][:counts[r]]) for r in range(3)))
        return answer
