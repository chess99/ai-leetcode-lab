# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        denavopelu = (position, time)
        prefix_time = [0]
        for value in time:
            prefix_time.append(prefix_time[-1] + value)

        # A state retains two consecutive signs: prev and current.  Their
        # indices determine the accumulated rate attached to current.
        states = {(-1, 0, 0): 0}
        for current in range(n - 1):
            layer = [(state, cost) for state, cost in states.items()
                     if state[1] == current]
            for (previous, marker, removed), cost_so_far in layer:
                if marker != current:
                    continue
                rate = prefix_time[marker + 1] - prefix_time[previous + 1]
                for nxt in range(marker + 1, n):
                    next_removed = removed + nxt - marker - 1
                    if next_removed > k:
                        break
                    cost = (cost_so_far
                            + (position[nxt] - position[marker]) * rate)
                    state = (marker, nxt, next_removed)
                    if cost < states.get(state, 10 ** 30):
                        states[state] = cost

        return min(cost for (previous, marker, removed), cost in states.items()
                   if marker == n - 1 and removed == k)
