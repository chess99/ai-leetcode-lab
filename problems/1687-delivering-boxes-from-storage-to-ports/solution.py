# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        changes = [0] * n
        for i in range(1, n):
            changes[i] = changes[i - 1] + (boxes[i][0] != boxes[i - 1][0])
        dp = [0] + [10 ** 9] * n
        from collections import deque
        candidates = deque([0])
        left = weight = 0
        for right in range(1, n + 1):
            weight += boxes[right - 1][1]
            while right - left > maxBoxes or weight > maxWeight:
                weight -= boxes[left][1]
                left += 1
            while candidates[0] < left:
                candidates.popleft()
            dp[right] = dp[candidates[0]] + changes[right - 1] - changes[candidates[0]] + 2
            if right < n:
                value = dp[right] - changes[right]
                while candidates and dp[candidates[-1]] - changes[candidates[-1]] >= value:
                    candidates.pop()
                candidates.append(right)
        return dp[n]
