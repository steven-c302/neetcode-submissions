class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0;
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        

        # walk through every element in the array using one pointer
        # annother pointer would track where the next "kept" element would go
        # if we find an element that isn't val, we would copy it to position k and then advance to k
        # if not val then just skip