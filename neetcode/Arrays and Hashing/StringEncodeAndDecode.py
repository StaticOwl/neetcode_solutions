class Solution:
    def encode(self, strs: List[str]) -> str:
        s = "&_>&".join(strs)
        if not s:
            return str(strs)
        return s

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        if s == "['']":
            return [""]
        return s.split("&_>&")