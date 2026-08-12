# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def validNumber(self, s: str) -> bool:
        s = s.strip(); seen_digit = seen_dot = seen_exp = False
        for i, ch in enumerate(s):
            if ch.isdigit(): seen_digit = True
            elif ch in '+-':
                if i and s[i - 1] not in 'eE': return False
            elif ch == '.':
                if seen_dot or seen_exp: return False
                seen_dot = True
            elif ch in 'eE':
                if seen_exp or not seen_digit: return False
                seen_exp = True; seen_digit = False
            else: return False
        return seen_digit
