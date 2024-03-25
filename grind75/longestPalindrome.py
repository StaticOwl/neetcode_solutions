#Logic: If count is even then add all, if count is more than one then just take the closest even count
# the flag is there because we can at max take one odd element, once that is taken, the others are ignored.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        track = {}
        count = 0
        flag = True
        for ch in s:
            if ch in track:
                track[ch] += 1
            else:
                track[ch] = 1
        
        for ch in track:
            print(ch)
            count += (track[ch] // 2)*2
            if track[ch]%2 == 1:
                if flag:
                    count +=1
                    flag = not flag

        return count