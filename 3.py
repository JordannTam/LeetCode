

import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        currLen = 0
        queue = collections.deque()

        for c in s:
            if c not in queue:
                queue.append(c)
                currLen += 1
                if currLen > longest:
                    longest = currLen
            else:
                while(c in queue):
                    curr = queue.popleft()
                    currLen -= 1
                queue.append(c)
                currLen += 1
        return longest
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        n = len(s)
        longest = 0

        for r in range(n):
            if s[r] not in charSet:
                charSet.add(s[r])
                # currLen += 1
            else:
                while(s[r] in charSet):
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
            longest = max(longest, r - l + 1)
        return longest


if __name__ == "__main__":
    s = Solution()
    print(Solution.lengthOfLongestSubstring(s, "jbpnbwwd"))
