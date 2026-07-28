class Solution:
   def encode(self, strs: List[str]) -> str:
       encoded_str = ""
       
       for word in strs:
           curr_str = ""
           for letter in word:
               letter_index = str(ord(letter) - ord('a'))
               curr_str += (letter_index + " ")
           
           encoded_str += (curr_str + "x")
       
       return encoded_str
   
   def decode(self, s: str) -> List[str]:
       output_list = []
       current_str = ""
       current_value = 0
       negative = False
       
       for num in s:
           if num == ' ':
               if negative:
                   current_value *= -1
                   negative = False
               
               character = chr(current_value + ord('a'))
               current_str += character
               
               current_value = 0
           elif num == 'x':
               output_list.append(current_str)
               current_str = ""
           else:
               if current_value:
                   current_value = current_value * 10
                   current_value += int(num)
               else:
                   if num == '-':
                       negative = True
                   else:
                       current_value += int(num)
       
       return output_list