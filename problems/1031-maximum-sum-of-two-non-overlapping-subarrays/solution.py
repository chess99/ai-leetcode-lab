# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:12:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = [0]
        for number in nums:
            prefix.append(prefix[-1] + number)

        def best_total(left_length: int, right_length: int) -> int:
            best_left = 0
            answer = 0
            for split in range(left_length, len(nums) - right_length + 1):
                best_left = max(best_left, prefix[split] - prefix[split - left_length])
                right_sum = prefix[split + right_length] - prefix[split]
                answer = max(answer, best_left + right_sum)
            return answer

        return max(best_total(firstLen, secondLen), best_total(secondLen, firstLen))
