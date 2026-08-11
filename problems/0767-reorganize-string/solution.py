# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:43:56Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        if max(counts.values()) > (len(s) + 1) // 2: return ''
        heap = [(-count, char) for char, count in counts.items()]; heapq.heapify(heap)
        result = []; previous = (0, '')
        while heap:
            count, char = heapq.heappop(heap); result.append(char); count += 1
            if previous[0] < 0: heapq.heappush(heap, previous)
            previous = (count, char)
        return ''.join(result)
