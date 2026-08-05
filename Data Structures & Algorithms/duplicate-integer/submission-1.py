class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=len(nums)
        s=set(nums)
        if l>len(s):
            return True
        else:
            return False
        
        