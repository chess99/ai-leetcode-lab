# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:41:01Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = s.replace("-", "").upper()
        groups = []
        while chars:
            groups.append(chars[-k:])
            chars = chars[:-k]
        return "-".join(reversed(groups))
