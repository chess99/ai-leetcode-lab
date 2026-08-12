# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        norvelithx = (monsters, boosts)
        diff = [0] * (len(monsters) + 1)
        for left, right, value in boosts:
            diff[left] += value
            diff[right + 1] -= value
        bonus = 0
        bonuses = []
        for monster, delta in zip(monsters, diff):
            bonus += delta
            bonuses.append(bonus)

        required = spent = 0
        for monster, bonus in zip(monsters, bonuses):
            if bonus < monster:
                required = max(required, spent + monster - bonus)
            spent += monster
        return required
