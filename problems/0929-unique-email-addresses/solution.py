# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:15:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            normalized.add(local + '@' + domain)
        return len(normalized)
