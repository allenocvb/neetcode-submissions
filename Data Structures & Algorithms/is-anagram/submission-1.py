class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s, dict_t = {}, {}
        for letter in range(len(s)):
            dict_s[s[letter]] = 1 + dict_s.get(s[letter], 0)
            dict_t[t[letter]] = 1 + dict_t.get(t[letter], 0)
        for item in dict_s:
            if dict_s[item] != dict_t.get(item, 0):
                return False
        return True