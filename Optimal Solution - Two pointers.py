'''
Algorithm:
  Initialize:
      Set maxi as the first character of the string: maxi = s[0].
      Set m as the guarenteed minimum answer of the string : m = 1. 
  
  Helper Function:
      
      Define a function helper(left, right) that:
      
              Takes two indices left and right which attempts to expand outwards from the center.
            
              While s[l] == s[r] (i.e., a palindrome), keep expanding:
    
                        Decrease l (move left).
                        
                        Increase r (move right).
              
              Stop when the substring no longer forms a palindrome or when the indices go out of bounds (i.e., l < 0 or r >= n).
              
              Return the substring from l + 1 to r - 1 (the valid palindromic substring) and its respective length which is given by r-(l+1) = r-l-1
  
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
            return  s[left + 1 : right ], r - l - 1     #The current longest palindromic substring centered at odd / even indices , The length of the current longest palindromic substring cenetred at odd / even indices.

        for i in range(n):
            candidate1 = helper(i, i + 1)  #ODD LENGTH PALINDROMIC SUBSTRING
            candidate2 = helper(i, i)      #EVEN LENGTH PALINDROMIC SUBSTRING
            if candidate1[1] >= candidate2[1]:
                if candidate1[1] > m :
                    maxi, m = candidate1   
            else:
                if candidate2[1] > m:
                    maxi, m = candidate2
        return maxi
