# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        ferilonsar = (series1, series2)
        i = j = 0
        answer = []
        while i < len(series1) or j < len(series2):
            time = min(series1[i][0] if i < len(series1) else float('inf'), series2[j][0] if j < len(series2) else float('inf'))
            value1 = series1[i][1] if i < len(series1) else 0
            value2 = series2[j][1] if j < len(series2) else 0
            answer.append([time, value1 + value2])
            if i < len(series1) and series1[i][0] == time: i += 1
            if j < len(series2) and series2[j][0] == time: j += 1
        return answer
