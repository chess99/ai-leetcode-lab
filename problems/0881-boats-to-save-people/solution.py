# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(); left=0; right=len(people)-1; boats=0
        while left<=right:
            if people[left]+people[right]<=limit: left+=1
            right-=1; boats+=1
        return boats
