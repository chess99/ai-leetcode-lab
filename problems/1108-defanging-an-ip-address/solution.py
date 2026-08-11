# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:30:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
