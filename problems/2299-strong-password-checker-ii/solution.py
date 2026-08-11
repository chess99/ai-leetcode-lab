# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:25:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        special = set('!@#$%^&*()-+')
        return len(password) >= 8 and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in special for c in password) and all(a != b for a, b in zip(password, password[1:]))
