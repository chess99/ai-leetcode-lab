# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:05:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        groups = {}
        for word in words:
            key = frozenset(word)
            groups[key] = groups.get(key, 0) + 1
        return sum(count * (count - 1) // 2 for count in groups.values())
