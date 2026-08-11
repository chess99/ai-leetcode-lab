# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:27:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import date
        return abs((date.fromisoformat(date1)-date.fromisoformat(date2)).days)
