class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        highest = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
                highest = max(highest, counter)
            else:
                counter = 0
        return highest

        # we need to walk through the entire array
        # everytime we find an 1 we set our counter to increase by 1
        # everytime we find an 0 we set out counter to 0
        # if our current counter is longer than our running highest than we update it
