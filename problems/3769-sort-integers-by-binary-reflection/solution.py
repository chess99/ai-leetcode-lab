# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:16:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def reflection(value: int) -> int:
            return int(bin(value)[:1:-1], 2)
        return sorted(nums, key=lambda value: (reflection(value), value))
