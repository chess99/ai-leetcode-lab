# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:29Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def beautySum(self, s: str) -> int:
        answer=0
        for i in range(len(s)):
            counts=[0]*26
            for char in s[i:]:
                counts[ord(char)-97]+=1;answer+=max(counts)-min(x for x in counts if x)
        return answer
