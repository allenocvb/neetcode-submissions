class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
        Time: O(nlogn)
        """
        if len(s) != len(t):
            return False

        s_check = {}
        t_check = {}
        for i in range(len(s)):
            s_check[s[i]] = 1 + s_check.get(s[i], 0)
            t_check[t[i]] = 1 + t_check.get(t[i], 0)
        
        return s_check == t_check



        