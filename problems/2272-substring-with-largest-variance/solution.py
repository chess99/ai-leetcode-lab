# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestVariance(self, s: str) -> int:
        characters = set(s)
        answer = 0
        for major in characters:
            for minor in characters:
                if major == minor:
                    continue
                major_count = 0
                minor_count = 0
                remaining_minor = s.count(minor)
                for character in s:
                    if character == major:
                        major_count += 1
                    elif character == minor:
                        minor_count += 1
                        remaining_minor -= 1
                    else:
                        continue
                    if minor_count:
                        answer = max(answer, major_count - minor_count)
                    if major_count < minor_count and remaining_minor:
                        major_count = minor_count = 0
        return answer
