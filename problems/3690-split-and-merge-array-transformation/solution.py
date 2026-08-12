# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque


class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        donquarist = (nums1, nums2)
        start, target = tuple(donquarist[0]), tuple(donquarist[1])
        if start == target:
            return 0
        queue = deque([(start, 0)])
        seen = {start}
        n = len(nums1)
        while queue:
            current, distance = queue.popleft()
            for left in range(n):
                for right in range(left, n):
                    segment = current[left:right + 1]
                    rest = current[:left] + current[right + 1:]
                    for position in range(len(rest) + 1):
                        following = rest[:position] + segment + rest[position:]
                        if following == target:
                            return distance + 1
                        if following not in seen:
                            seen.add(following)
                            queue.append((following, distance + 1))
        return -1
