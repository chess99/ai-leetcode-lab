# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:42Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List

class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        lorquandis = (value, limit)
        groups = defaultdict(list)
        for gain, threshold in zip(*lorquandis):
            groups[threshold].append(gain)
        answer = 0
        for threshold, gains in groups.items():
            gains.sort(reverse=True)
            answer += sum(gains[:threshold])
        return answer
