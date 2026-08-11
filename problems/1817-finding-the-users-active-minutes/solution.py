# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:32Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        minutes=defaultdict(set)
        for user,minute in logs:minutes[user].add(minute)
        answer=[0]*k
        for values in minutes.values():answer[len(values)-1]+=1
        return answer
