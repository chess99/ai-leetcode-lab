# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        probabilities = [0.0] * (n + 1)
        probabilities[0] = 1.0
        window = 1.0
        result = 0.0
        for score in range(1, n + 1):
            probabilities[score] = window / maxPts
            if score < k:
                window += probabilities[score]
            else:
                result += probabilities[score]
            if score >= maxPts:
                window -= probabilities[score - maxPts]
        return result
