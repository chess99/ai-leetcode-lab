# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:32:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        return sum(max(day.count(char) for day in demand) for char in 'abcdefghijklmnopqrstuvwxyz')
