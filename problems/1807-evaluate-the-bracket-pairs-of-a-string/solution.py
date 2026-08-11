# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        values=dict(knowledge);answer=[];i=0
        while i<len(s):
            if s[i]!='(':answer.append(s[i]);i+=1;continue
            end=s.index(')',i);answer.append(values.get(s[i+1:end],'?'));i=end+1
        return ''.join(answer)
