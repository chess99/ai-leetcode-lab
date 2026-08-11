# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks=[]
        for word in words:
            mask=0
            for c in word: mask|=1<<(ord(c)-97)
            masks.append(mask)
        return max((len(words[i])*len(words[j]) for i in range(len(words)) for j in range(i) if not masks[i]&masks[j]),default=0)
