# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:58:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = blocks[:k].count('W')
        best = white
        for i in range(k, len(blocks)):
            white += (blocks[i] == 'W') - (blocks[i-k] == 'W')
            best = min(best, white)
        return best
