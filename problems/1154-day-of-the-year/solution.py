# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:27:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def dayOfYear(self, date: str) -> int:
        year,month,day=map(int,date.split('-')); days=[31,28,31,30,31,30,31,31,30,31,30,31]
        if year%400==0 or year%4==0 and year%100: days[1]=29
        return sum(days[:month-1])+day
