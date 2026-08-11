# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countHousePlacements(self, n: int) -> int:
        modulo = 10**9 + 7
        ends_empty = 1
        ends_with_house = 0

        for _ in range(n):
            ends_empty, ends_with_house = (
                (ends_empty + ends_with_house) % modulo,
                ends_empty,
            )

        one_side = (ends_empty + ends_with_house) % modulo
        return one_side * one_side % modulo
