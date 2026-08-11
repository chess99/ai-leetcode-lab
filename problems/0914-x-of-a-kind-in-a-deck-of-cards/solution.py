# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:15:47Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        group_size = 0
        for count in Counter(deck).values():
            group_size = gcd(group_size, count)
        return group_size >= 2
