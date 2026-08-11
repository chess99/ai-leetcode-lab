# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:30Z
# Experiment: ai-leetcode-lab, round 1
class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.expires_at = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expires_at[tokenId] = currentTime + self.time_to_live

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.expires_at.get(tokenId, 0) > currentTime:
            self.expires_at[tokenId] = currentTime + self.time_to_live

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(expiration > currentTime for expiration in self.expires_at.values())
