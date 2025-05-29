class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # The table of elements we will need
        need = {}

        for i in t:
            need[i] = need.get(i, 0) + 1
        
        #Number of unique elements
        need_count = len(need)


        window = {}
        have = 0



        res_len = float('inf')
        res_start = 0
        
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                curr_len = right - left + 1

                if curr_len < res_len:
                    res_start = left
                    res_len = curr_len
                
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:

                    have -= 1
                left += 1
        
        if res_len == float("inf"):
            return ""
        return s[res_start : (res_start + res_len)]

