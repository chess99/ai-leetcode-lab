# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        size = len(nums)
        changes = [0] * size
        score = 0
        for index, value in enumerate(nums):
            if value <= index:
                score += 1
            lose = (index - value + 1) % size
            regain = (index + 1) % size
            changes[lose] -= 1
            changes[regain] += 1
            if lose > regain:
                changes[0] -= 1
        best_score = score
        answer = 0
        for rotation in range(1, size):
            score += changes[rotation]
            if score > best_score:
                best_score = score
                answer = rotation
        return answer
