class Solution:

    def encode(self, strs: List[str]) -> str:

        decoded_string = ""
        for string in strs:
            decoded_string += str(len(string)) + "#" + string

        return decoded_string

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length_number = int(s[i:j])
            result.append(s[j+1: j+1+length_number])
            i = j+1+length_number
        return result
