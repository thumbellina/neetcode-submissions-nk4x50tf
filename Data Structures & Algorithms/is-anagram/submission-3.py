class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # only smaller case so initiate alpha array of 26 size 0 initiated, loop through array and add for s and negate for t and check if each is 0
        if len(s) != len(t):
            return False
        alpha_arr = [0]*26
        for alpha in range(0, len(s)):
            alpha_arr[ord(s[alpha])- ord('a')] += 1
            alpha_arr[ord(t[alpha]) - ord('a')] -= 1
        for num in alpha_arr:
            if num != 0:
                return False
        return True



        