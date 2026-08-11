# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:27:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        result = []
        for value in arr:
            result.append(value)
            if value == 0:
                result.append(0)
        arr[:] = result[:len(arr)]
