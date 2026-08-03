class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        count = 0
        for x in nums:
            if count + 1 < len(nums) and nums[count] == nums[count + 1]:
                return True
            else:
                count += 1
        return False