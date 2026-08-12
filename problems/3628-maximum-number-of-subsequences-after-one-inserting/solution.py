# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        count_l = count_lc = count_lct = 0
        for char in s:
            if char == 'L':
                count_l += 1
            elif char == 'C':
                count_lc += count_l
            elif char == 'T':
                count_lct += count_lc

        add_l = 0
        count_t = 0
        for char in reversed(s):
            if char == 'T':
                count_t += 1
            elif char == 'C':
                add_l += count_t

        add_t = count_lc
        best_c = 0
        left_l = 0
        right_t = s.count('T')
        for char in s:
            best_c = max(best_c, left_l * right_t)
            if char == 'L':
                left_l += 1
            elif char == 'T':
                right_t -= 1
        best_c = max(best_c, left_l * right_t)
        return count_lct + max(add_l, add_t, best_c)
