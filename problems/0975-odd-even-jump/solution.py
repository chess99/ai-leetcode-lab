# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:05Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        size = len(arr)

        def following(order):
            result = [-1] * size
            stack = []
            for index in order:
                while stack and index > stack[-1]:
                    result[stack.pop()] = index
                stack.append(index)
            return result

        odd_next = following(sorted(range(size), key=lambda index: (arr[index], index)))
        even_next = following(sorted(range(size), key=lambda index: (-arr[index], index)))
        odd = [False] * size
        even = [False] * size
        odd[-1] = even[-1] = True
        for index in range(size - 2, -1, -1):
            if odd_next[index] >= 0:
                odd[index] = even[odd_next[index]]
            if even_next[index] >= 0:
                even[index] = odd[even_next[index]]
        return sum(odd)
