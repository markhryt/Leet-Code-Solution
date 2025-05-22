/*

The approach to this problem is the following:
    If we can get to an index i, it means we can get to any index before i.
    Therefore, it makes sense to track the furthest index we can reach.
    So, after going through the whole array, if the furthest index exceeds(we allow it in our interpretation)
    the index of last element in the array, it means that we can reach the last index, and return True.
*/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True


        furthestSoFar = nums[0]

        for i in range(0, len(nums)):
            if i <= furthestSoFar and i + nums[i] > furthestSoFar:
                furthestSoFar = i + nums[i]

        return furthestSoFar >= len(nums)-1



/*
    I also though of another solution. Even though it is not optimal it is still interesting from the point of view of
    sheer practice. So I decided to include it here. This solution  involved using a dynamic programming table, tracking
     reachability of every element in the array, and based on the reachability status of the last element
     we would make our decision. Although not optimal here, it could be the solution for a situation with fixed size
     of a jump.
*/


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        if len(nums) <= 1:
            return True
    
        dt = [False] * len(nums)

        dt[0] = True

        for i in range(0, len(nums)):
            if(dt[i]):
                for j in range(1, nums[i] + 1):
                    if(i + j < len(nums)):
                        dt[i + j] = True
    
        return dt[-1]

