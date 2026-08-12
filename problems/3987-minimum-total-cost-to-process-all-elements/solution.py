# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        sovalemrin = (nums, k)
        resource = k
        operations = answer = 0
        for value in nums:
            if resource < value:
                extra = (value - resource + k - 1) // k
                answer += extra * (2 * operations + extra + 1) // 2
                operations += extra
                resource += extra * k
            resource -= value
        return answer % 1_000_000_007
