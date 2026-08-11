# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:14:04Z
# Experiment: ai-leetcode-lab, round 1
class Codec:

    def __init__(self):
        self.urls = {}
        self.encoded = {}
        self.next_id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encoded:
            short_url = "http://tinyurl.com/" + str(self.next_id)
            self.next_id += 1
            self.encoded[longUrl] = short_url
            self.urls[short_url] = longUrl
        return self.encoded[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
