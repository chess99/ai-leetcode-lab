# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        nexoraviml = nums
        n = len(nums)
        left = [1] * n
        for index in range(1, n):
            current = (nums[index] > nums[index - 1]) - (nums[index] < nums[index - 1])
            previous = ((nums[index - 1] > nums[index - 2])
                        - (nums[index - 1] < nums[index - 2])) if index >= 2 else 0
            if current:
                left[index] = 2
                if index == 1 or current != previous:
                    left[index] = left[index - 1] + 1

        right = [1] * n
        for index in range(n - 2, -1, -1):
            current = (nums[index + 1] > nums[index]) - (nums[index + 1] < nums[index])
            following = ((nums[index + 2] > nums[index + 1])
                         - (nums[index + 2] < nums[index + 1])) if index + 2 < n else 0
            if current:
                right[index] = 2
                if index + 2 == n or current != following:
                    right[index] = right[index + 1] + 1

        answer = max(left)
        for removed in range(1, n - 1):
            bridge = ((nums[removed + 1] > nums[removed - 1])
                      - (nums[removed + 1] < nums[removed - 1]))
            if not bridge:
                continue
            left_ok = (left[removed - 1] == 1 or bridge != (
                (nums[removed - 1] > nums[removed - 2])
                - (nums[removed - 1] < nums[removed - 2])))
            right_ok = (right[removed + 1] == 1 or bridge != (
                (nums[removed + 2] > nums[removed + 1])
                - (nums[removed + 2] < nums[removed + 1])))
            if left_ok:
                answer = max(answer, left[removed - 1] + 1)
            if right_ok:
                answer = max(answer, 1 + right[removed + 1])
            if left_ok and right_ok:
                answer = max(answer, left[removed - 1] + right[removed + 1])
        return answer
