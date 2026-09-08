class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        total = sum(nums[:n-1])
        for i in range (n-1,1,-1):
           if total > nums[i]:
            return total+ nums[i]
           total -=nums[i-1]
        return -1     