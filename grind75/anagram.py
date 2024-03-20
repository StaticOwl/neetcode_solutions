#pretty easy solution
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

#Wanted to not use sorted as sort algorithms have their own time complexities, this is O(n)
def isAnagram(self, s: str, t: str) -> bool:
        elementMap = {}
        for ch in s:
            if ch not in elementMap:
                elementMap[ch] = 1
            else:
                elementMap[ch] += 1
        for ch in t:
            if ch not in elementMap:
                return False
            else:
                if elementMap[ch] == 0:
                    return False
                elif elementMap[ch] == 1:
                    del elementMap[ch]
                else:
                    elementMap[ch] -= 1
        
        return True if not elementMap else False