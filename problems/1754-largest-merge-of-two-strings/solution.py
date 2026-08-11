# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        first = second = 0
        merge = []

        while first < len(word1) and second < len(word2):
            if word1[first:] > word2[second:]:
                merge.append(word1[first])
                first += 1
            else:
                merge.append(word2[second])
                second += 1

        merge.append(word1[first:])
        merge.append(word2[second:])
        return "".join(merge)
