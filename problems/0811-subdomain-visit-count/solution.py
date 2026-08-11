# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:46:08Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = Counter()
        for entry in cpdomains:
            count, domain = entry.split()
            labels = domain.split(".")
            for index in range(len(labels)):
                counts[".".join(labels[index:])] += int(count)
        return [f"{count} {domain}" for domain, count in counts.items()]
