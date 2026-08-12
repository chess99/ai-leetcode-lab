# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:47Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def maxGroupNumber(self, tiles: List[int]) -> int:
        counts = Counter(tiles)
        states = {(0, 0): 0}
        previous = None
        for value in sorted(counts):
            if previous is None or value != previous + 1:
                states = {(0, 0): states.get((0, 0), 0)}
            count = counts[value]
            next_states = {}
            for (started_two_ago, started_one_ago), groups in states.items():
                mandatory = started_two_ago + started_one_ago
                if mandatory > count:
                    continue
                for newly_started in range(min(2, count - mandatory) + 1):
                    current = groups + started_two_ago
                    current += (count - mandatory - newly_started) // 3
                    state = (started_one_ago, newly_started)
                    next_states[state] = max(next_states.get(state, -1), current)
            states = next_states
            previous = value
        return states.get((0, 0), 0)
