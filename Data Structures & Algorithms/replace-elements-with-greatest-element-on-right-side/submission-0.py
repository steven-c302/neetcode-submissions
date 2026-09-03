class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # go through the entire array and see if it's the largest
        for i in range(len(arr)):
            max = 0
            for j in range(i + 1, len(arr)):
                if max < arr[j]:
                    max = arr[j]
                arr[i] = max
        # set last element to be -1
        arr[len(arr) - 1] = -1

        return arr