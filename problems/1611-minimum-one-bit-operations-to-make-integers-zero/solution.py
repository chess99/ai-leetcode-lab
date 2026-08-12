# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        answer=0
        while n:answer^=n;n>>=1
        return answer
