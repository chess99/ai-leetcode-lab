# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:09:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [index for index, value in enumerate(sorted(nums)) if value == target]
