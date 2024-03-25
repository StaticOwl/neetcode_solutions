# Keeping Track of count of elements in magazine then checking ransomNote for occurrences exist in track
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        track = {}
        for ch in magazine:
            if ch in track:
                track[ch] += 1
            else:
                track[ch] = 1
        
        for ch in ransomNote:
            if ch not in track:
                return False
            else:
                if track[ch] == 0:
                    return False
                else:
                    track[ch] -= 1
        
        return True

#No Extra Space Solution:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch not in magazine:
                return False
            magazine = magazine.replace(ch, '', 1)
        return True 