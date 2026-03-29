"""

LC: 443. String Compression

Medium

Topics
Two Pointers
String

Hint
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
962,305/1.6M
Acceptance Rate
59.0%

Hint 1
How do you know if you are at the end of a consecutive group of characters?

"""

class Solution:
    def compress(self,chars:list[str]) -> int:
        i = 0
        j = 0
        while j<len(chars):
            char = chars[j]
            count=0
            while j<len(chars) and chars[j]==char:
                j+=1
                count+=1
            chars[i]=char
            i+=1
            if count>1:
                for c in str(count):
                    chars[i]=c
                    i+=1
        return i,chars[:i]
sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c"]))
print(sol.compress(["a"]))
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))


#-----------------------EXPLANATION-------------------------
class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0  # 'i' is the write pointer → where we place compressed characters
        j = 0  # 'j' is the read pointer → used to scan through the list
        
        # Continue until we read all characters
        while j < len(chars):
            char = chars[j]   # store the current character
            count = 0         # count how many times this character repeats
            
            # Count all consecutive occurrences of the same character
            while j < len(chars) and chars[j] == char:
                j += 1        # move read pointer ahead
                count += 1    # increment repetition count
            
            # Write the character at current write position
            chars[i] = char
            i += 1            # move write pointer forward
            
            # If count > 1, we need to write the digits of the count
            if count > 1:
                for c in str(count):  # convert count into individual characters
                    chars[i] = c      # write each digit
                    i += 1            # move write pointer forward
        
        # return the new length after compression
        return i
