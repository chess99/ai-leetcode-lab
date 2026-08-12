# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        modulus = 1_000_000_007

        def prime_score(value):
            score = 0
            divisor = 2
            while divisor * divisor <= value:
                if value % divisor == 0:
                    score += 1
                    while value % divisor == 0:
                        value //= divisor
                divisor += 1
            return score + (value > 1)

        scores = [prime_score(value) for value in nums]
        size = len(nums)
        previous = [-1] * size
        stack = []
        for index, score in enumerate(scores):
            while stack and scores[stack[-1]] < score:
                stack.pop()
            if stack:
                previous[index] = stack[-1]
            stack.append(index)
        following = [size] * size
        stack = []
        for index in range(size - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[index]:
                stack.pop()
            if stack:
                following[index] = stack[-1]
            stack.append(index)

        answer = 1
        for value, index in sorted(((value, index) for index, value in enumerate(nums)),
                                   reverse=True):
            choices = (index - previous[index]) * (following[index] - index)
            used = min(k, choices)
            answer = answer * pow(value, used, modulus) % modulus
            k -= used
            if k == 0:
                break
        return answer
