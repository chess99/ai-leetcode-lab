# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:00:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters=[]; digits=[]
        for log in logs:
            (letters if log.split()[1].isalpha() else digits).append(log)
        return sorted(letters,key=lambda log:(log.split()[1:],log.split()[0]))+digits
