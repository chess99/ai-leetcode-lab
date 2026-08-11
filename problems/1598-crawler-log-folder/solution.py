# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:06:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth=0
        for log in logs:
            if log=='../':depth=max(0,depth-1)
            elif log!='./':depth+=1
        return depth
