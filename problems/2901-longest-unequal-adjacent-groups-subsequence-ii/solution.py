# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        parent = [-1] * len(words)
        length = [1] * len(words)
        for right in range(len(words)):
            for left in range(right):
                if groups[left] != groups[right] and len(words[left]) == len(words[right]) and sum(a != b for a, b in zip(words[left], words[right])) == 1 and length[left] + 1 > length[right]:
                    length[right] = length[left] + 1
                    parent[right] = left
        index = max(range(len(words)), key=length.__getitem__)
        answer = []
        while index != -1:
            answer.append(words[index])
            index = parent[index]
        return answer[::-1]
