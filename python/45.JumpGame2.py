class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0


        current_limit = 0
        price = 0
        max_range = 0

        for i in range(len(nums) - 1):

            max_range = max(max_range, nums[i] + i)

            if i == current_limit:
                price+=1
                current_limit = max_range

        return price
