# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def entityParser(self, text: str) -> str:
        for entity, character in (("&quot;", '"'), ("&apos;", "'"), ("&gt;", ">"), ("&lt;", "<"), ("&frasl;", "/"), ("&amp;", "&")):
            text = text.replace(entity, character)
        return text
