# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:32:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def runeReserve(self, runes: List[int]) -> int:
        runes.sort()
        best = current = 1
        for i in range(1, len(runes)):
            current = current + 1 if runes[i] - runes[i - 1] <= 1 else 1
            best = max(best, current)
        return best
