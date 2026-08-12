# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:59Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
import heapq


class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        nivarotelu = (nums, k, m)
        positions = defaultdict(list)
        count = defaultdict(int)
        left_distinct = 0
        threshold = {}
        minimum_heap = []
        answer = 0

        for right, value in enumerate(nums):
            positions[value].append(right)
            count[value] += 1
            threshold[value] = (positions[value][-m]
                                if len(positions[value]) >= m else -1)
            heapq.heappush(minimum_heap, (threshold[value], value))

            while len(count) > k:
                removed = nums[left_distinct]
                count[removed] -= 1
                if count[removed] == 0:
                    del count[removed]
                left_distinct += 1

            while minimum_heap and (
                    minimum_heap[0][1] not in count
                    or threshold[minimum_heap[0][1]] != minimum_heap[0][0]):
                heapq.heappop(minimum_heap)
            if len(count) == k and minimum_heap and minimum_heap[0][0] >= left_distinct:
                answer += minimum_heap[0][0] - left_distinct + 1
        return answer
