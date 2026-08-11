# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:08:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        groups = {}
        for char, count in counts.items():
            groups.setdefault(count, []).append(char)

        return "".join(max(groups.values(), key=lambda chars: (len(chars), counts[chars[0]])))
