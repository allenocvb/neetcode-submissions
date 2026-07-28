class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = [0] * 26
        longest_repeating = 0

        for r in range(len(s)):
            count[ord(s[r]) - ord("A")] += 1

            while ((r-l+1) - max(count)) > k:
                count[ord(s[l]) - ord("A")] -= 1
                l += 1

            longest_repeating = max(longest_repeating, r-l+1) 

        return longest_repeating 

        