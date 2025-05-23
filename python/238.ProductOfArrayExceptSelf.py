class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)

        k = 1

        for i in range(1, len(nums)):
            k *= nums[i-1]
            ans[i] = k

        r = 1

        for i in range(len(nums) - 2, -1, -1):
            r *= nums[i + 1]
            ans[i] *= r

        return ans