# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:07:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        counts = Counter((s1 + ' ' + s2).split())
        return [word for word, count in counts.items() if count == 1]
