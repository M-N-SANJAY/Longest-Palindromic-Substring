'''
Algorithm:
  Initialize:
      Set maxi as the first character of the string: maxi = s[0].
      Set m as the guarenteed minimum answer of the string : m = 1. 
  
  Helper Function:
      
      Define a function helper(left, right) that:
      
              Takes two indices left and right which attempts to expand outwards from the center.
            
              While s[left] == s[right] (i.e., a palindrome), keep expanding:
    
                        Decrease left (move left).
                        
                        Increase right (move right).
              
              Stop when the substring no longer forms a palindrome or when the indices go out of bounds (i.e., l < 0 or r >= n).
              
              Return the substring from l + 1 to r - 1 (the valid palindromic substring) and its respective length which is given by right-(left+1) = right-left-1
  
  Main Loop: Iterate through each possible center of the palindrome:
  
  For each index i in the range 0 to n-1:
  
  Call helper(i, i) to find the longest palindrome centered at a single character (odd-length palindromes).
  
  Call helper(i, i + 1) to find the longest palindrome centered at a pair of adjacent characters (even-length palindromes).
  
  Update maxi to the longest of the three candidates: maxi, helper(i, i), and helper(i, i + 1).
  
  Output: Return the longest palindromic substring, stored in maxi.

'''
def longest_palindromic_substring(self, s):  #You should ignore the self parameter if you do not refer to any class instances guys, remember that.
       
        n = len(s)    # The length of the given input string
        maxi = s[0]   # Records the longest palindromic substring time-to-time
        m = 1         # Records the length of the longest palindromic substring time-to-time  
  
        def helper(left, right):                     
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome in range left+1 to right-1
            return  s[left + 1 : right ], right - left - 1     #The current longest palindromic substring centered at odd / even indices , The length of the current longest palindromic substring cenetred at odd / even indices.

        for i in range(n):
            candidate1 = helper(i, i + 1)  #EVEN LENGTH PALINDROMIC SUBSTRING
            candidate2 = helper(i, i)      #ODD LENGTH PALINDROMIC SUBSTRING
            if candidate1[1] >= candidate2[1]:
                if candidate1[1] > m :
                    maxi, m = candidate1   
            else:
                if candidate2[1] > m:
                    maxi, m = candidate2
        return maxi
'''
Complexities:

Time Complexity: O(n²) 
The function calls helper for each character in the string which means n times helper is called, and helper may take up to O(n) time.
which makes it O(n)*O(n)=O(n²)

Space Complexity: O(n)
The space required for storing string slices during the palindrome check.


'''
