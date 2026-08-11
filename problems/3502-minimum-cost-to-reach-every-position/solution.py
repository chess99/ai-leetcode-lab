# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:03:55Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        answer = []
        minimum = float("inf")
        for value in cost:
            minimum = min(minimum, value)
            answer.append(minimum)
        return answer
