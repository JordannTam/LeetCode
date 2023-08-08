class Solution:
    # Attempt 1
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1

        for x in t:
            if x not in d:
                return False
            d[x] -= 1
            if d[x] == 0:
                d.pop(x)

        if d != {}:
            return False
        return True

    # Attempt 2

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for c in set(s):
            if s.count(c) != t.count(c):
                return False
        return True
