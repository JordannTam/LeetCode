

class Solution:
    def removeNthFromEnd(self, ls):

        dp = []

        for _ in range(len(ls) + 1):
            ls = []
            for _ in range(len(ls) + 1):
                ls.append(0)
            dp.append(ls)


