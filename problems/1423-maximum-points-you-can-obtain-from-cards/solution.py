# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score = sum(cardPoints[:k])
        best = score
        for taken_from_right in range(1, k + 1):
            score -= cardPoints[k - taken_from_right]
            score += cardPoints[-taken_from_right]
            best = max(best, score)
        return best
