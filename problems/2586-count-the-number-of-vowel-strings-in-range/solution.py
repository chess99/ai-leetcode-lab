# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:07:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set('aeiou')
        return sum(word[0] in vowels and word[-1] in vowels for word in words[left:right + 1])
