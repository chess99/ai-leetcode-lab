# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumDeletions(self, s: str) -> int:
        delete_b=answer=0
        for char in s:
            if char=='b':delete_b+=1
            else:answer=min(answer+1,delete_b)
        return answer
