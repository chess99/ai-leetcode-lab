# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:47:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        counts = [[0] * 11 for _ in range(n)]
        for player, color in pick:
            counts[player][color] += 1
        return sum(any(count > player for count in counts[player]) for player in range(n))
