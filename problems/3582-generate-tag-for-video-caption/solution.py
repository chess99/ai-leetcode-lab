# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:04:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words:
            return "#"

        tag = words[0].lower() + "".join(word.capitalize() for word in words[1:])
        return ("#" + "".join(char for char in tag if char.isalpha()))[:100]
