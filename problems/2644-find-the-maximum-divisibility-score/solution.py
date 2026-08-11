# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:07:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        best_score = -1; answer = float('inf')
        for divisor in divisors:
            score = sum(value % divisor == 0 for value in nums)
            if score > best_score or (score == best_score and divisor < answer): best_score, answer = score, divisor
        return answer
