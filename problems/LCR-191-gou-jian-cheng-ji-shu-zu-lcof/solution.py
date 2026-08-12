# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def statisticalResult(self, arrayA: List[int]) -> List[int]:
        length = len(arrayA)
        answer = [1] * length
        prefix = 1
        for index in range(length):
            answer[index] = prefix
            prefix *= arrayA[index]
        suffix = 1
        for index in range(length - 1, -1, -1):
            answer[index] *= suffix
            suffix *= arrayA[index]
        return answer
