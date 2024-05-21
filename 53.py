class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_output = 0
        maximum = float('-inf')


        for i in nums:
            max_output += i
            if maximum < max_output:
                maximum = max_output
            if max_output < 0:
                max_output = 0

        return maximum