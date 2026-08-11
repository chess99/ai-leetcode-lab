# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = set()
        answer = 0
        for value in nums:
            if value in seen:
                answer ^= value
            else:
                seen.add(value)
        return answer
