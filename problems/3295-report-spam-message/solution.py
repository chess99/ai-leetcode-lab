# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
  b=set(bannedWords);return sum(x in b for x in message)>=2
