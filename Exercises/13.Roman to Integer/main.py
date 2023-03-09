class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "IIIIIIIII")
        
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "XXXXXXXXX")
        
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "CCCCCCCCC")
        
        s_sum = 0
        s_reversed = s[::-1]
        
        for letter in s_reversed:
            s_sum += roman_values[letter]
        return s_sum
            
roman_values = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
}
