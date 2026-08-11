# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        first,second=sentence1.split(),sentence2.split()
        if len(first)>len(second):first,second=second,first
        left=0
        while left<len(first) and first[left]==second[left]:left+=1
        right=0
        while right<len(first)-left and first[-1-right]==second[-1-right]:right+=1
        return left+right==len(first)
