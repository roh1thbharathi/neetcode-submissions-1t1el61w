class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countt = {}
        for char in t:
            countt[char] = 1 + countt.get(char, 0)

        def contains_all(window_str):
            # Create a dictionary for the window and compare it to countt
            window_count = {}
            for char in window_str:
                window_count[char] = 1 + window_count.get(char, 0)
            
            for char in countt:
                if window_count.get(char, 0) < countt[char]:
                    return False
            return True

        # Brute-force approach to check all possible substrings
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                window_str = s[i:j+1]
                if contains_all(window_str):
                    # Update result if this window is smaller
                    if res == "" or len(window_str) < len(res):
                        res = window_str

        return res
