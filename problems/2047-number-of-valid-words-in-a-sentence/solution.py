# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:04:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countValidWords(self, sentence: str) -> int:
        import re
        return sum(bool(re.fullmatch(r'(?:[a-z]+(?:-[a-z]+)?[!.,]?|[!.,])', word)) for word in sentence.split())
