class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target_index = len(nums)-1

        for i in range(target_index-1, -1, -1):
            if target_index<=i+nums[i]:
                target_index = i

        if target_index == 0:
            return True

        return False
