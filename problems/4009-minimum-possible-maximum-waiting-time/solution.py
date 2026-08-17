# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        telmorvian = (demand, fuel)
        # At the release time of the next car, keep each pump's remaining
        # busy time.  Absolute timestamps are unnecessary and would create
        # far too many distinct states.
        # (used fuel of pump 0, busy time 0, busy time 1) -> best max wait
        states = {(0, 0, 0): 0}
        used_total = 0
        answer = -1

        for amount in demand:
            next_states = {}
            for (used0, busy0, busy1), maximum_wait in states.items():
                used1 = used_total - used0

                if used0 + amount <= fuel[0]:
                    wait = busy0
                    state = (used0 + amount, amount,
                             max(0, busy1 - wait))
                    value = max(maximum_wait, wait)
                    if value < next_states.get(state, 10 ** 9):
                        next_states[state] = value

                if used1 + amount <= fuel[1]:
                    wait = busy1
                    state = (used0, max(0, busy0 - wait), amount)
                    value = max(maximum_wait, wait)
                    if value < next_states.get(state, 10 ** 9):
                        next_states[state] = value

            if not next_states:
                break
            states = next_states
            used_total += amount
            answer = min(states.values())

        return answer
