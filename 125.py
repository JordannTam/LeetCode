import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = re.sub("[^a-z0-9]*", "", s.lower())
        return a == "".join(reversed(a))

    # my attempt
    # def isPalindrome(self, s: str) -> bool:
    #     a = "".join(re.split("[^a-zA-Z0-9]*", s)).lower()
    #     for i in range(int(len(a) / 2)):
    #         if a[i] != a[-i - 1]:
    #             return False
    #     return True


if __name__ == "__main__":
    s = Solution()
    print(Solution.isPalindrome(s, "A man, a plan, a canal: Panama"))
