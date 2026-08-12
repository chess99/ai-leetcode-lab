# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        string_index = pattern_index = 0
        star_index = -1
        star_match = 0
        while string_index < len(s):
            if (pattern_index < len(p)
                    and (p[pattern_index] == '?'
                         or p[pattern_index] == s[string_index])):
                string_index += 1
                pattern_index += 1
            elif pattern_index < len(p) and p[pattern_index] == '*':
                star_index = pattern_index
                star_match = string_index
                pattern_index += 1
            elif star_index >= 0:
                star_match += 1
                string_index = star_match
                pattern_index = star_index + 1
            else:
                return False
        return all(char == '*' for char in p[pattern_index:])
