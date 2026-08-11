# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:39Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        def find(email):
            parent.setdefault(email, email)
            if parent[email] != email: parent[email] = find(parent[email])
            return parent[email]
        for account in accounts:
            first = account[1]
            for email in account[1:]: parent[find(email)] = find(first)
        groups = defaultdict(list)
        for email in parent: groups[find(email)].append(email)
        names = {account[1]: account[0] for account in accounts}
        return [[names[root]] + sorted(emails) for root, emails in groups.items()]
