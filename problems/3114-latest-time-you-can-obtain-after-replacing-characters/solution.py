# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findLatestTime(self, s: str) -> str:
        for hour in range(11, -1, -1):
            for minute in range(59, -1, -1):
                candidate = f"{hour:02d}:{minute:02d}"
                if all(source == "?" or source == target for source, target in zip(s, candidate)):
                    return candidate
        return ""
