# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:31Z
# Experiment: ai-leetcode-lab, round 1
from functools import cmp_to_key
from typing import List


class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        enemies = [((life + power - 1) // power, attack)
                   for life, attack in zip(health, damage)]

        def compare(first, second):
            return first[0] * second[1] - second[0] * first[1]

        enemies.sort(key=cmp_to_key(compare))
        remaining_damage = sum(damage)
        answer = 0
        for attacks, attack in enemies:
            answer += remaining_damage * attacks
            remaining_damage -= attack
        return answer
