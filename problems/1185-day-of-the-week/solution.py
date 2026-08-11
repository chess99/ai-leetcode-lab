# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:41:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = day - 1
        for current_year in range(1971, year):
            days += 366 if current_year % 400 == 0 or (current_year % 4 == 0 and current_year % 100 != 0) else 365
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            months[1] = 29
        days += sum(months[:month - 1])
        return ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"][days % 7]
