# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        red, yellow, final_red = (leaves[0] == 'y'), 10 ** 9, 10 ** 9
        for char in leaves[1:]:
            to_red = char == 'y'
            to_yellow = char == 'r'
            final_red = min(yellow, final_red) + to_red
            yellow = min(red, yellow) + to_yellow
            red += to_red
        return final_red
