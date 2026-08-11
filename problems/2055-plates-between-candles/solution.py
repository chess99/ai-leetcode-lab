# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:19Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        plates_prefix = [0] * (n + 1)
        nearest_left = [-1] * n
        nearest_right = [-1] * n
        last_candle = -1
        for index, char in enumerate(s):
            if char == "|":
                last_candle = index
            nearest_left[index] = last_candle
            plates_prefix[index + 1] = plates_prefix[index] + (char == "*")
        last_candle = -1
        for index in range(n - 1, -1, -1):
            if s[index] == "|":
                last_candle = index
            nearest_right[index] = last_candle
        answer = []
        for left_bound, right_bound in queries:
            left_candle = nearest_right[left_bound]
            right_candle = nearest_left[right_bound]
            if left_candle == -1 or right_candle == -1 or left_candle >= right_candle:
                answer.append(0)
            else:
                answer.append(plates_prefix[right_candle] - plates_prefix[left_candle])
        return answer
