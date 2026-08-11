# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def required(target: int) -> int:
            arr = nums[:]
            moves = 0
            for i in range(len(arr) - 1):
                if arr[i] != target:
                    arr[i] = -arr[i]; arr[i + 1] = -arr[i + 1]
                    moves += 1
            return moves if arr[-1] == target else 10**9
        return min(required(1), required(-1)) <= k
