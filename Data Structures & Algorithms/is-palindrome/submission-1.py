class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = "".join(char.lower() for char in s if char.isalnum())
        k = len(test) - 1
        for i in range(len(test) // 2):
            if test[i] == test[k]:

                k -= 1
            else:
                return False
        return True

    # two pointers, one at the start and one at the end