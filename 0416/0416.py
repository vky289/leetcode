class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        dp = set()
        dp.add(0)
        target = total_sum // 2

        for i in range(len(nums) - 1, 0, -1):
            clone_dp = set(list(dp))
            for t in dp:
                if t + nums[i] == target:
                    return True
                clone_dp.add(t + nums[i])
            dp = clone_dp

        return True if target in dp else False