class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        s1_sorted = sorted(s1)          # sorted() returns a new list

        for i in range(m - n + 1):      # covers all windows including the first
            tmp = sorted(s2[i:i+n])     # slice exactly n chars, then sort
            if s1_sorted == tmp:        # compare sorted window to sorted s1
                return True

        return False