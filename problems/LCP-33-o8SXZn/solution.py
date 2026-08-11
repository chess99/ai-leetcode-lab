# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:27:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        maximum_vat = max(vat)
        if maximum_vat == 0:
            return 0

        result = float("inf")
        for fills in range(1, maximum_vat + 1):
            upgrades = sum(max(0, (need + fills - 1) // fills - capacity) for capacity, need in zip(bucket, vat))
            result = min(result, upgrades + fills)
        return result
