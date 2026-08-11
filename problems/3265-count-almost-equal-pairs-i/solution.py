# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def variants(value: int) -> set[int]:
            digits = list(str(value))
            result = {value}
            for left in range(len(digits)):
                for right in range(left + 1, len(digits)):
                    digits[left], digits[right] = digits[right], digits[left]
                    result.add(int(''.join(digits)))
                    digits[left], digits[right] = digits[right], digits[left]
            return result

        answer = 0
        for index, value in enumerate(nums):
            possible = variants(value)
            answer += sum(other in possible for other in nums[:index])
        return answer
