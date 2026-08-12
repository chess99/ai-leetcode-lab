# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxDistance(self, moves: str) -> int:
        horizontal = moves.count('R') - moves.count('L')
        vertical = moves.count('U') - moves.count('D')
        return abs(horizontal) + abs(vertical) + moves.count('_')
