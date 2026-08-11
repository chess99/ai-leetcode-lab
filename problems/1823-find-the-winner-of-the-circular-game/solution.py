# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner=0
        for size in range(1,n+1):winner=(winner+k)%size
        return winner+1
