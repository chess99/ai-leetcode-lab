# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:52:12Z
# Experiment: ai-leetcode-lab, round 1
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.position = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.position + 1]
        self.history.append(url)
        self.position += 1

    def back(self, steps: int) -> str:
        self.position = max(0, self.position - steps)
        return self.history[self.position]

    def forward(self, steps: int) -> str:
        self.position = min(len(self.history) - 1, self.position + steps)
        return self.history[self.position]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
