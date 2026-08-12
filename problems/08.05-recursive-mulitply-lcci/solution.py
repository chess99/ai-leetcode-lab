# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:55Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A > B:
            A, B = B, A
        answer = 0
        while A:
            if A & 1:
                answer += B
            A >>= 1
            B <<= 1
        return answer
