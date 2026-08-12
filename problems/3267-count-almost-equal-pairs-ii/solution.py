# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:34Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        width = max(len(str(value)) for value in nums)
        seen: dict[int, int] = defaultdict(int)
        answer = 0

        for value in nums:
            digits = list(f'{value:0{width}d}')
            variants = {value}
            first_swaps = {''.join(digits)}

            for first in range(width):
                for second in range(first + 1, width):
                    digits[first], digits[second] = digits[second], digits[first]
                    first_swaps.add(''.join(digits))
                    digits[first], digits[second] = digits[second], digits[first]

            for state in first_swaps:
                current = list(state)
                variants.add(int(state))
                for first in range(width):
                    for second in range(first + 1, width):
                        current[first], current[second] = current[second], current[first]
                        variants.add(int(''.join(current)))
                        current[first], current[second] = current[second], current[first]

            answer += sum(seen[candidate] for candidate in variants)
            seen[value] += 1

        return answer
