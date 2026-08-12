# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        spent=answer=0
        for actual,minimum in sorted(tasks,key=lambda task:task[1]-task[0],reverse=True):answer=max(answer,spent+minimum);spent+=actual
        return answer
