# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen=set(); answer=[]; part=''
        for char in s:
            part += char
            if part not in seen:
                seen.add(part); answer.append(part); part=''
        return answer
