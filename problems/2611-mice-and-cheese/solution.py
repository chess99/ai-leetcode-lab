# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        return sum(reward2) + sum(sorted((a - b for a, b in zip(reward1, reward2)), reverse=True)[:k])
