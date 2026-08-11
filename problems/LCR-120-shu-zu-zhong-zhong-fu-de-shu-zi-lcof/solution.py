# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:39:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        seen = set()
        for document in documents:
            if document in seen:
                return document
            seen.add(document)
        return -1
