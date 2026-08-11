# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lengths = {0: 0}
        longest = 0
        for line in input.split("\n"):
            depth = len(line) - len(line.lstrip("\t"))
            name = line[depth:]
            length = lengths[depth] + len(name)
            if "." in name:
                longest = max(longest, length)
            else:
                lengths[depth + 1] = length + 1
        return longest
