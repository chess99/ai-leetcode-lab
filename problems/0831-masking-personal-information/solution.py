# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.lower().split("@")
            return name[0] + "*****" + name[-1] + "@" + domain
        digits = "".join(char for char in s if char.isdigit())
        country = "" if len(digits) == 10 else "+" + "*" * (len(digits) - 10) + "-"
        return country + "***-***-" + digits[-4:]
