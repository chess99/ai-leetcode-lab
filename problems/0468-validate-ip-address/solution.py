# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:08:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_ipv4() -> bool:
            parts = queryIP.split(".")
            return len(parts) == 4 and all(
                part.isdigit()
                and not (len(part) > 1 and part[0] == "0")
                and 0 <= int(part) <= 255
                for part in parts
            )

        def is_ipv6() -> bool:
            hexadecimal = set("0123456789abcdefABCDEF")
            parts = queryIP.split(":")
            return len(parts) == 8 and all(
                1 <= len(part) <= 4 and all(char in hexadecimal for char in part)
                for part in parts
            )

        if "." in queryIP and is_ipv4():
            return "IPv4"
        if ":" in queryIP and is_ipv6():
            return "IPv6"
        return "Neither"
