class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()

        for i in range(0,len(nums)):
            if (target - nums[i]) in a:
                return [a[target-nums[i]],i]

            a[nums[i]]=i