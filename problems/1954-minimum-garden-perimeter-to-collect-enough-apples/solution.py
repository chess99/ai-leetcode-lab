# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        radius = 0
        apples = 0

        while apples < neededApples:
            radius += 1
            apples += 12 * radius * radius

        return 8 * radius
