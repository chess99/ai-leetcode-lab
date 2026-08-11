# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:23:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        common = Counter(words[0])
        for word in words[1:]: common &= Counter(word)
        return list(common.elements())
