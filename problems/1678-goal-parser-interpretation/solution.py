# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:19:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')
