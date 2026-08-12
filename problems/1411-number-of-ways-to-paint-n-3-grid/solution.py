# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numOfWays(self, n: int) -> int:
        modulus = 1_000_000_007
        two_colors = three_colors = 6
        for _ in range(1, n):
            two_colors, three_colors = (
                (3 * two_colors + 2 * three_colors) % modulus,
                (2 * two_colors + 2 * three_colors) % modulus)
        return (two_colors + three_colors) % modulus
