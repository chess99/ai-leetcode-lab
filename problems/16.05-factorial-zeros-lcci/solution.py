# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:00:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer = 0
        while n:
            n //= 5
            answer += n
        return answer
