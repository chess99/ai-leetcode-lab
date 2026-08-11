# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        import heapq

        counts = [0] * 26
        for char in s:
            if char != '?':
                counts[ord(char) - ord('a')] += 1
        heap = [(counts[index], index) for index in range(26)]
        heapq.heapify(heap)
        chosen = []
        for char in s:
            if char == '?':
                count, index = heapq.heappop(heap)
                chosen.append(index)
                heapq.heappush(heap, (count + 1, index))
        chosen.sort()
        iterator = iter(chosen)
        return ''.join(chr(next(iterator) + ord('a')) if char == '?' else char for char in s)
