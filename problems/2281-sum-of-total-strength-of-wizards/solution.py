# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        modulus = 10 ** 9 + 7
        size = len(strength)
        left = [-1] * size
        stack = []
        for index, value in enumerate(strength):
            while stack and strength[stack[-1]] >= value:
                stack.pop()
            left[index] = stack[-1] if stack else -1
            stack.append(index)

        right = [size] * size
        stack = []
        for index in range(size - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[index]:
                stack.pop()
            right[index] = stack[-1] if stack else size
            stack.append(index)

        prefix = [0]
        for value in strength:
            prefix.append((prefix[-1] + value) % modulus)
        prefix_of_prefix = [0]
        for value in prefix:
            prefix_of_prefix.append((prefix_of_prefix[-1] + value) % modulus)

        answer = 0
        for index, value in enumerate(strength):
            left_count = index - left[index]
            right_count = right[index] - index
            right_sum = (
                prefix_of_prefix[right[index] + 1]
                - prefix_of_prefix[index + 1]
            ) % modulus
            left_sum = (
                prefix_of_prefix[index + 1]
                - prefix_of_prefix[left[index] + 1]
            ) % modulus
            contribution = right_sum * left_count - left_sum * right_count
            answer = (answer + value * contribution) % modulus
        return answer
