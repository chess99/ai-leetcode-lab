# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = group_sum = largest = 0
        for i,time in enumerate(neededTime):
            if i and colors[i] != colors[i - 1]:
                answer += group_sum - largest
                group_sum = largest = 0
            group_sum += time
            largest = max(largest, time)
        return answer + group_sum - largest
