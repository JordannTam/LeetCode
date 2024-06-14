from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # if len(height) <= 2:
        #     return 0
        # l = 0
        # r = len(height) - 1
        # result = 0
        # lmax = 0
        # rmax = 0
        # while l <= r:
        #     if lmax < height[l]:
        #         lmax = height[l]
        #     if rmax < height[r]:
        #         rmax = height[r]

        #     if lmax <= rmax:
        #         result += lmax - height[l]
        #         l += 1
        #     else:
        #         result += rmax - height[r]
        #         r -= 1

        # return result













        l = 0
        r = len(height) - 1
        result = 0
        lmax = 0
        rmax = 0

        
        while l < r:
            print(l, r)
            if height[l] > lmax:
                lmax = height[l]
            if height[r] > rmax:
                rmax = height[r]

            
            if lmax < rmax:
                result += lmax - height[l]
                l += 1
            else:
                result += rmax - height[r]
                r -= 1
        return result



if __name__ == "__main__":
    s = Solution()
    print(Solution.trap(s, [4,2,0,3,2,5]))
