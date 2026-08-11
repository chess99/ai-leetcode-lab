# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:00:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort(); left = 0; right = len(tokens) - 1; score = best = 0
        while left <= right:
            if power >= tokens[left]: power -= tokens[left]; left += 1; score += 1; best = max(best, score)
            elif score: power += tokens[right]; right -= 1; score -= 1
            else: break
        return best
