# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:53:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used={};answer=[]
        for name in names:
            if name not in used:used[name]=1;answer.append(name);continue
            suffix=used[name]
            while f'{name}({suffix})' in used:suffix+=1
            new=f'{name}({suffix})';used[name]=suffix+1;used[new]=1;answer.append(new)
        return answer
