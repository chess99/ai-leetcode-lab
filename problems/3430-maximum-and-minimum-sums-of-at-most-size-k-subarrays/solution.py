# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def pair_count(left: int, right: int) -> int:
            left = min(left, k)
            full = min(left, max(0, k + 1 - right))
            answer = full * right
            remaining = left - full
            if remaining:
                first = k - full
                last = k - left + 1
                answer += remaining * (first + last) // 2
            return answer

        def contribution(is_minimum: bool) -> int:
            previous = [-1] * n
            stack = []
            for i, value in enumerate(nums):
                while stack and ((nums[stack[-1]] >= value) if is_minimum else (nums[stack[-1]] <= value)):
                    stack.pop()
                previous[i] = stack[-1] if stack else -1
                stack.append(i)

            following = [n] * n
            stack.clear()
            for i in range(n - 1, -1, -1):
                value = nums[i]
                while stack and ((nums[stack[-1]] > value) if is_minimum else (nums[stack[-1]] < value)):
                    stack.pop()
                following[i] = stack[-1] if stack else n
                stack.append(i)

            return sum(
                value * pair_count(i - previous[i], following[i] - i)
                for i, value in enumerate(nums)
            )

        return contribution(True) + contribution(False)
