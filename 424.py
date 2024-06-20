import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "AABABBA" k = 1
        #  L  R
        if len(s) == 0:
            return 0
        n = len(s)
        l = 0
        longestChar = s[0]
        counter = collections.Counter()
        result = 0
        for r in range(n):
            counter[s[r]] += 1
            while(r - l + 1 - max(counter.values()) > k):
                counter[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(Solution.characterReplacement(s, s = "AAAAABBBBCBB", k = 4))
