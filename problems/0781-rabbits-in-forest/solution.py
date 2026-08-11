# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:43:58Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from math import ceil
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum((answer + 1) * ceil(count / (answer + 1)) for answer, count in Counter(answers).items())
