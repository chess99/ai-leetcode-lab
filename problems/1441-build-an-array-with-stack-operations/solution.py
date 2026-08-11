# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:51:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer=[]; current=1
        for value in target:
            while current<value: answer += ['Push','Pop']; current+=1
            answer.append('Push'); current+=1
        return answer
