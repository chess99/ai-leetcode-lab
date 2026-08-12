# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:01:01Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        changes = [0] * 102
        for born, died in zip(birth, death):
            changes[born - 1900] += 1
            changes[died - 1900 + 1] -= 1
        alive = best_alive = 0
        answer = 1900
        for offset, change in enumerate(changes):
            alive += change
            if alive > best_alive:
                best_alive = alive
                answer = 1900 + offset
        return answer
