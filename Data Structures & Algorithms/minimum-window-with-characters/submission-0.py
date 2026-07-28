class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t:
            return ""
        
        requirements, window = {}, {}
        requirements = Counter(t)
        have, need = 0, len(requirements)
        res, res_len = [-1,-1], float("inf")
        l = 0

        for r in range(len(s)):

            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in requirements and requirements[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:

                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                window[s[l]] -= 1

                if s[l] in requirements and window[s[l]] < requirements[s[l]]:
                    have -= 1

                l += 1
                
        l, r = res
        
        return s[l:r+1] if res_len != float("inf") else ""



        
        
        