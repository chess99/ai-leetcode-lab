# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:42:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result=[]; previous=None
        for word in words:
            current=''.join(sorted(word))
            if current != previous: result.append(word)
            previous=current
        return result
