# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: x, n = 1 / x, -n
        answer = 1.0
        while n:
            if n & 1: answer *= x
            x *= x; n >>= 1
        return answer
