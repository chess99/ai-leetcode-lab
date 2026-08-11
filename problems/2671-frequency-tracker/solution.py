# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
class FrequencyTracker:
    def __init__(self): self.count=defaultdict(int); self.freq=defaultdict(int)
    def add(self, number: int) -> None:
        old=self.count[number]; self.freq[old]-=1 if old else 0; self.count[number]=old+1; self.freq[old+1]+=1
    def deleteOne(self, number: int) -> None:
        old=self.count[number]
        if old: self.freq[old]-=1; self.count[number]=old-1; self.freq[old-1]+=1 if old>1 else 0
    def hasFrequency(self, frequency: int) -> bool: return self.freq[frequency]>0
