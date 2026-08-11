# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:16Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        best_score = 0
        best_mask = 0

        for mask in range(1 << 12):
            arrows_needed = 0
            score = 0
            for region in range(12):
                if mask & (1 << region):
                    arrows_needed += aliceArrows[region] + 1
                    score += region
            if arrows_needed <= numArrows and score > best_score:
                best_score = score
                best_mask = mask

        answer = [0] * 12
        arrows_used = 0
        for region in range(12):
            if best_mask & (1 << region):
                answer[region] = aliceArrows[region] + 1
                arrows_used += answer[region]
        answer[0] += numArrows - arrows_used
        return answer
