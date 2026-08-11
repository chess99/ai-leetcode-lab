# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result, in_block, line = [], False, []
        for text in source:
            index = 0
            if not in_block: line = []
            while index < len(text):
                if not in_block and text[index:index+2] == '//': break
                if not in_block and text[index:index+2] == '/*': in_block = True; index += 2
                elif in_block and text[index:index+2] == '*/': in_block = False; index += 2
                elif not in_block: line.append(text[index]); index += 1
                else: index += 1
            if not in_block and line: result.append(''.join(line))
        return result
