# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:52:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter
        return all(count % len(words) == 0 for count in Counter(''.join(words)).values())
