class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sN = len(s)
        tN = len(t)
        l = 0
        matches = 0
        res = s + ":2:4"

        if tN > sN:
            return ""
        sCount = [0] * 128
        tCount = [0] * 128

        for i in range(tN):
            tCount[ord(t[i])] += 1
            if tCount[ord(t[i])] != 0 :
                sCount[ord(s[i])] += 1
        
        for i in range(128):
            if sCount[i] >= tCount[i]:
                matches += 1
        if matches == 128:
            return s[0:tN]
        
        for i in range(tN, sN):
            if tCount[ord(s[i])] != 0 :
                sCount[ord(s[i])] += 1
                if sCount[ord(s[i])] == tCount[ord(s[i])]:
                    matches += 1
            while(matches == 128):
                if len(s[l:i + 1]) < len(res):
                    res = s[l:i + 1]
                if tCount[ord(s[l])] != 0 :
                    if sCount[ord(s[l])] == tCount[ord(s[l])]:
                        matches -= 1
                    sCount[ord(s[l])] -= 1
                l += 1
        if res == s + ":2:4":
            return ""
        return res






        
if __name__ == "__main__":
    s = Solution()
    print(Solution.minWindow(s, s = "bba", t = "ab"))
