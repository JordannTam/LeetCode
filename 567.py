import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
        s2Count = [0] * 26
        matches = 0
        n = len(s1)
        totalN = len(s2)

        for i in range(n):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(n):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        if matches == 26:
            return True
        
        matches = 0

        for i in range(n, totalN):
            if s2Count[ord(s2[i - n]) - ord('a')] == s1Count[ord(s1[i - n]) - ord('a')]:
                matches -= 1
            s2Count[ord(s2[i]) - ord('a')] += 1
            s2Count[ord(s2[i - n]) - ord('a')] -= 1
            if s2Count[ord(s2[i]) - ord('a')] == s1Count[ord(s1[i]) - ord('a')]:
                matches += 1
            if matches == 26:
                return True
        return False

        
if __name__ == "__main__":
    s = Solution()
    print(Solution.checkInclusion(s, s1 = "adc", s2 = "dadc"))
