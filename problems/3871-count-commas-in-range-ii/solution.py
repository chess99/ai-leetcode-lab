# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countCommas(self, n: int) -> int:
        nalverqito = n
        answer = 0
        threshold = 1_000
        commas = 1
        while threshold <= n:
            next_threshold = threshold * 1_000
            answer += (min(n, next_threshold - 1) - threshold + 1) * commas
            threshold = next_threshold
            commas += 1
        return answer
