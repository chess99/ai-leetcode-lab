# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:24Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack: list[tuple[int, int]] = []
        answer = 0

        for value in nums:
            steps = 0
            while stack and value >= stack[-1][0]:
                steps = max(steps, stack.pop()[1])
            if stack:
                steps += 1
            stack.append((value, steps))
            answer = max(answer, steps)

        return answer
