# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:23Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        records=defaultdict(list)
        for name,time in zip(keyName,keyTime):
            hour,minute=map(int,time.split(':'));records[name].append(hour*60+minute)
        answer=[]
        for name,times in records.items():
            times.sort()
            if any(times[i+2]-times[i]<=60 for i in range(len(times)-2)):answer.append(name)
        return sorted(answer)
