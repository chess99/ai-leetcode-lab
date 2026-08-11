# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        positions = {}
        for left in range(len(s)):
            value = 0
            for right in range(left, min(len(s), left + 30)):
                value = (value << 1) | (s[right] == "1")
                candidate = [left, right]
                previous = positions.get(value)
                if previous is None or right - left < previous[1] - previous[0]:
                    positions[value] = candidate
        return [positions.get(first ^ second, [-1, -1]) for first, second in queries]
