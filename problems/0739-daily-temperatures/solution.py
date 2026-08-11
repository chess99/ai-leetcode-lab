# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        waiting = []
        for index, temperature in enumerate(temperatures):
            while waiting and temperatures[waiting[-1]] < temperature:
                previous = waiting.pop()
                answer[previous] = index - previous
            waiting.append(index)
        return answer
