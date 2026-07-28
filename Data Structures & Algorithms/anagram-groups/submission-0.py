from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        First approach: here we iterate through array and sorted the string.
        Then we taked the sorted and append the string we are looking at to its
        values. So smoothly do this since we have a defaultdict which initializes
        all keys with an array. We know the anagram should be grouped together if
        when sorted, they are the same. 
        Time complexity: O(m * nlogn)
        Space complexity: O(m * n)

        Code:

        result = defaultdict(list)

        for stringg in strs:
            sorted_stringg = ''.join(sorted(stringg))
            result[sorted_stringg].append(stringg)
        
        return result.values()
        """


        #########################################################################

        """
        we iterate through array and for each string, and we create a count array
        which starts with 26 0's in the array. For each letter in string we are 
        looking at, we will increase the index of what every position represents
        that number. we can do this by using ord(letter) - ord('a'). Since like
        ord('a') - ord('a') = 0(this index represents a). So in turn, 
        something like ord('b') which would be like 81 and ord('a') which would
        be like 80 would give us 1(this index represents b). So after going through
        that string, we add that count tuple to the dictionary and add the string
        to its list. Remember we initialized with defaultdict(list). Lastly we
        return the results.values().
        """
        results = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for letter in string:
                count[ord(letter) - ord('a')] += 1
            
            results[tuple(count)].append(string)
        
        return (results.values())


        