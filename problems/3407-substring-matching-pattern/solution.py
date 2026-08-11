# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:59:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split('*')
        for start in range(len(s) - len(prefix) + 1):
            if not s.startswith(prefix, start):
                continue
            end = s.find(suffix, start + len(prefix))
            if end != -1 and end + len(suffix) > start:
                return True
        return False
