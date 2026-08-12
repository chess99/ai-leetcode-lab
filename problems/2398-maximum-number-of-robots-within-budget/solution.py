# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:51Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        maximum = deque()
        running_sum = 0
        left = 0
        answer = 0
        for right, (charge, cost) in enumerate(zip(chargeTimes, runningCosts)):
            running_sum += cost
            while maximum and chargeTimes[maximum[-1]] <= charge:
                maximum.pop()
            maximum.append(right)
            while (maximum and chargeTimes[maximum[0]]
                   + (right - left + 1) * running_sum > budget):
                if maximum[0] == left:
                    maximum.popleft()
                running_sum -= runningCosts[left]
                left += 1
            answer = max(answer, right - left + 1)
        return answer
