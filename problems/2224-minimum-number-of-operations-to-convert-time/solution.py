# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:18:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def minutes(value):
            hour,minute=map(int,value.split(':'));return hour*60+minute
        difference=minutes(correct)-minutes(current); operations=0
        for step in [60,15,5,1]:
            count,difference=divmod(difference,step);operations+=count
        return operations
