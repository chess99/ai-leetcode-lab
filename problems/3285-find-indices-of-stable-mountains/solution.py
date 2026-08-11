# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [index for index in range(1, len(height)) if height[index - 1] > threshold]
