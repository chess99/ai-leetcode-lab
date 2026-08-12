# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        planted = 0
        answer = 0
        for grow, plant in sorted(zip(growTime, plantTime), reverse=True):
            planted += plant
            answer = max(answer, planted + grow)
        return answer
