# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:08:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        take=min(k,numOnes);score=take;k-=take;take=min(k,numZeros);k-=take;return score-k
