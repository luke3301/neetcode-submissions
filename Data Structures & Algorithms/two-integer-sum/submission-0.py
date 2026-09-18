class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if (nums[i] not in hash) and ((target - nums[i]) not in hash):
                hash[nums[i]] = i
            elif (target - nums[i]) in hash:
                return[hash[target - nums[i]], i]