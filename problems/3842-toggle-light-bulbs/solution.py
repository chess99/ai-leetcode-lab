# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:18:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        active = set()
        for bulb in bulbs:
            if bulb in active: active.remove(bulb)
            else: active.add(bulb)
        return sorted(active)
