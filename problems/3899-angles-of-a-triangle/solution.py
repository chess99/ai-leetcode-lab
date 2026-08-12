# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        import math

        norqavelid = sorted(sides)
        if norqavelid[0] + norqavelid[1] <= norqavelid[2]:
            return []

        angles = []
        for i in range(3):
            opposite = norqavelid[i]
            adjacent1 = norqavelid[(i + 1) % 3]
            adjacent2 = norqavelid[(i + 2) % 3]
            cosine = (adjacent1 ** 2 + adjacent2 ** 2 - opposite ** 2) / (2 * adjacent1 * adjacent2)
            cosine = min(1.0, max(-1.0, cosine))
            angles.append(math.degrees(math.acos(cosine)))
        return sorted(angles)
