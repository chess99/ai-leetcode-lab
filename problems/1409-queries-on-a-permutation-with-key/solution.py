# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        values = list(range(1,m+1)); answer=[]
        for query in queries:
            index=values.index(query); answer.append(index)
            values.insert(0,values.pop(index))
        return answer
