class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleanedString = ""

        for letter in s:
            if letter.isalnum():
                cleanedString += letter.lower()
        
        return cleanedString == cleanedString[::-1]
        