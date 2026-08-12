# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        length = len(password)
        missing = 3 - sum((any(c.islower() for c in password),
                           any(c.isupper() for c in password),
                           any(c.isdigit() for c in password)))
        runs = []
        index = 0
        while index < length:
            following = index
            while following < length and password[following] == password[index]:
                following += 1
            if following - index >= 3:
                runs.append(following - index)
            index = following
        replacements = sum(run // 3 for run in runs)
        if length < 6:
            return max(6 - length, missing)
        if length <= 20:
            return max(replacements, missing)
        deletions = length - 20
        remaining = deletions
        for remainder in range(3):
            for index, run in enumerate(runs):
                if run < 3 or run % 3 != remainder:
                    continue
                use = min(remaining, remainder + 1)
                runs[index] -= use
                remaining -= use
                if remaining == 0:
                    break
            if remaining == 0:
                break
        replacements = sum(run // 3 for run in runs)
        replacements -= min(replacements, remaining // 3)
        return deletions + max(missing, replacements)
