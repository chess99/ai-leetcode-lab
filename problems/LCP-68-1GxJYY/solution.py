# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import defaultdict


class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        frequency = defaultdict(int)
        left = 0
        answer = 0
        for right, flower in enumerate(flowers):
            frequency[flower] += 1
            while frequency[flower] > cnt:
                frequency[flowers[left]] -= 1
                left += 1
            answer += right - left + 1
        return answer
