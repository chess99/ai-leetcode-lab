# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maximum = answer = 0
        for index, flip in enumerate(flips, 1):
            maximum = max(maximum, flip)
            if maximum == index: answer += 1
        return answer
