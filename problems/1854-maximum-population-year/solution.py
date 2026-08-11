# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:32:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years=[0]*101
        for birth,death in logs:
            for year in range(birth,death):years[year-1950]+=1
        return 1950+years.index(max(years))
