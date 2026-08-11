# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:19Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times=times; self.leaders=[]; counts={}; leader=-1
        for person in persons:
            counts[person]=counts.get(person,0)+1
            if counts[person]>=counts.get(leader,0): leader=person
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        return self.leaders[bisect_right(self.times,t)-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
