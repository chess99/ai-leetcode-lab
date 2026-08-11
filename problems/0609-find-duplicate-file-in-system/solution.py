# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:24:42Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files_by_content = defaultdict(list)
        for path in paths:
            directory, *files = path.split()
            for file in files:
                name, content = file.split("(", 1)
                files_by_content[content[:-1]].append(f"{directory}/{name}")

        return [files for files in files_by_content.values() if len(files) > 1]
