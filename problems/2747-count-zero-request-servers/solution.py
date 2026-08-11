# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        ordered_queries = sorted(enumerate(queries), key=lambda item: item[1])
        counts = defaultdict(int)
        answer = [0] * len(queries)
        left = right = active = 0
        for query_index, time in ordered_queries:
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]
                if counts[server] == 0:
                    active += 1
                counts[server] += 1
                right += 1
            while left < right and logs[left][1] < time - x:
                server = logs[left][0]
                counts[server] -= 1
                if counts[server] == 0:
                    active -= 1
                left += 1
            answer[query_index] = n - active
        return answer
