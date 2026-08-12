# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:38Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        varelunixo = nums
        maximums = deque()
        minimums = deque()
        left = 0
        answer = 0
        for right, value in enumerate(varelunixo):
            while maximums and varelunixo[maximums[-1]] <= value:
                maximums.pop()
            while minimums and varelunixo[minimums[-1]] >= value:
                minimums.pop()
            maximums.append(right)
            minimums.append(right)
            while (varelunixo[maximums[0]] - varelunixo[minimums[0]]) * (right - left + 1) > k:
                if maximums[0] == left:
                    maximums.popleft()
                if minimums[0] == left:
                    minimums.popleft()
                left += 1
            answer += right - left + 1
        return answer
