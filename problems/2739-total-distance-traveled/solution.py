# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:22:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        while mainTank:
            used = min(mainTank, 5)
            mainTank -= used; distance += used * 10
            if used == 5 and additionalTank:
                mainTank += 1; additionalTank -= 1
        return distance
