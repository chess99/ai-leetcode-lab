# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:27:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reformatDate(self, date: str) -> str:
        day,month,year=date.split(); months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        return f'{year}-{months.index(month)+1:02d}-{int(day[:-2]):02d}'
