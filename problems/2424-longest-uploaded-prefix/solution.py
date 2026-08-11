# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:16Z
# Experiment: ai-leetcode-lab, round 1
class LUPrefix:
    def __init__(self, n: int): self.uploaded=[False]*(n+2); self.prefix=0
    def upload(self, video: int) -> None:
        self.uploaded[video]=True
        while self.uploaded[self.prefix+1]: self.prefix+=1
    def longest(self) -> int: return self.prefix
