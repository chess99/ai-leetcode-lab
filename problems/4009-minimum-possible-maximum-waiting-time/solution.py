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
        # state: (used fuel 0, used fuel 1, free time 0, free time 1,
        #         release time of next car) -> minimum maximum wait
        states = {(0, 0, 0, 0, 0): 0}
        best_count = 0
        best_wait = -1
        for index, amount in enumerate(demand):
            next_states = {}
            for (used0, used1, free0, free1, release), maximum_wait in states.items():
                for pump in range(2):
                    used = used0 if pump == 0 else used1
                    if used + amount > fuel[pump]:
                        continue
                    free = free0 if pump == 0 else free1
                    start = max(release, free)
                    wait = start - release
                    if pump == 0:
                        state = (used0 + amount, used1, start + amount,
                                 free1, start)
                    else:
                        state = (used0, used1 + amount, free0,
                                 start + amount, start)
                    value = max(maximum_wait, wait)
                    if value < next_states.get(state, 10 ** 9):
                        next_states[state] = value
            if not next_states:
                break
            states = next_states
            best_count = index + 1
            best_wait = min(states.values())
        return best_wait if best_count else -1
