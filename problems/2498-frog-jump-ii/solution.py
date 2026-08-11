# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxJump(self, stones: List[int]) -> int:
        answer = stones[1] - stones[0]
        for index in range(2, len(stones)):
            answer = max(answer, stones[index] - stones[index - 2])
        return answer
