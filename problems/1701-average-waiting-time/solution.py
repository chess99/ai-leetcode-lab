# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish=waiting=0
        for arrival,time in customers:
            finish=max(finish,arrival)+time;waiting+=finish-arrival
        return waiting/len(customers)
