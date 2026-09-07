# ≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠SOTI≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠

#ARRAY

#17/8/2026
#1.TWO SUM

def twoSum(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
print(twoSum([2,7,11,15],26))

def twoSum(nums,target):
    hashmap={}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement],i]
        else:
            hashmap[num] = i
print(twoSum([2,3,6,5,8],13))


#9.PALINDROME NUMBER
def palindrome(num):
    return str(num) == str(num)[::-1]
print(palindrome(12321))


#13.ROMAN TO INTEGER
def romanToInt(s):
    res=0
    roman={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    for i in range(len(s)):
        if i<len(s)-1 and roman[s[i]]<roman[s[i+1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res
print(romanToInt("MCMXCIV"))
            

#12.INTEGER TO ROMAN
def intToRoman(num):
    res=""
    roman_map={
        1000:"M",
        900:"CM",
        500:"D",
        400:"CD",
        100:"C",
        90:"XC",
        50:"L",
        40:"XL",
        10:"X",
        9:"IX",
        5:"V",
        4:"IV",
        1:"I"    
    }
    for number,roman in roman_map.items():
        while num>=number:
            res+=roman
            num-=number
    return res
print(intToRoman(1994))
  
"""         
Mistake:
    since we are comparing like this: "while num >= number:", need to keep the key of the dictionary as the num itself, not as string.
    if you are using thhe dictionary use .items()
    The list of tuples is generally preferred:

roman_map = [
    (1000, "M"),
    (900, "CM"),
    ...
]

Reasons:

✅ The order is explicit and guaranteed.
✅ It makes it clear that the values are processed from largest to smallest.
✅ It's the standard solution you'll see for LeetCode 12 (Integer to Roman).

"""

#14. Longest Common Prefix
def longestCommonPrefix(s):
    if len(s)==0:
        return ""
    base=s[0]
    for i in range(len(base)):
        for word in s[1:]:
            if i==len(word) or base[i]!=word[i]:
                return base[:i]
    return base
print(longestCommonPrefix(["flower","flow","flight"]))

#or

def longestCommonPrefix(s):
    s.sort()
    first=s[0]
    last=s[-1]
    i=0
    while i<len(first) and first[i]==last[i]:
        i+=1
    return first[:i]
print(longestCommonPrefix(["flower","flow","flight"]))


#283.MOVE ZEROES
def moveZeroes(nums):
    left=0
    for right in range(len(nums)):
        if nums[right]!=0:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
    return nums
print(moveZeroes([0,1,0,3,12,0]))


#26.REMOVE DUPLICATES FROM SORTED ARRAY
def removeDuplicates(nums):
    left=0
    for right in range(1,len(nums)):
        if nums[left]!=nums[right]:
            left+=1
            nums[left] = nums[right]
    return left+1
print(removeDuplicates([1,1,2,3,3,4]))


#27.REMOVE ELEMENTS
def removeElements(nums,val):
    left=0
    for right in range(len(nums)):
        if nums[right]!=val:
            nums[left]=nums[right]
            left+=1
    return nums[:left]
print(removeElements([3,2,2,3,5,3], 3))


#18/8/26

#58.Length of last word
def lengthLastWord(s):
    words=s.split()
    return len(words[-1])
print(lengthLastWord("I saw a canals on my way"))

#or
def lengthOfLastWord(s):
    length=0
    i=len(s)-1
    while i>=0 and s[i]==' ':
        i-=1
    while i>=0 and s[i]!=' ':
        i-=1
        length+=1
    return length
print(lengthOfLastWord("I tookk a selfie with Sir.Lewis Hamilton at the British GP in 2028 "))
            

#125.VALID PALINDROME
def validPalindromeI(s):
    left,right = 0,len(s)-1
    while left<right:
        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        if s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
    return True
    # return False
print(validPalindromeI(s = "A man, a plan, a canal: Panama"))
print(validPalindromeI("race a car"))
    

#680.VALID PALINDROME II
def validPalindromII(s):
    def isPalindrome(s,left,right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    left,right=0,len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return isPalindrome(s,left+1,right) or isPalindrome(s,left,right-1)
        left+=1
        right-=1
    return True
print(validPalindromII(s = "abca"))

#53.MAXIMUM SUBARRAY
def maxSubarray(nums):
    current_max=nums[0]
    global_max=nums[0]
    for i in range(1,len(nums)):
        current_max=max(nums[i],current_max+nums[i])
        global_max=max(global_max,current_max)
    return global_max
print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))

#16.VALID ANAGRAMS
def validAnagram(s,t):
    s_freq={}
    t_freq={}
    for ch in s:
        if ch not in s_freq:
            s_freq[ch]=1
        s_freq[ch]+=1
    for ch in t:
        if ch not in t_freq:
            t_freq[ch]=1
        t_freq[ch]+=1
    return s_freq==t_freq
print(validAnagram(s = "anagram", t = "nagaram"))


#46.GROUP ANAGRAMS
from collections import defaultdict
def groupAnagrams(s):
    group=defaultdict(list)
    for word in s:
        key=''.join(sorted(word))
        group[key].append(word)
    return list(group.values())
print(groupAnagrams(s = ["eat","tea","tan","ate","nat","bat"]))

#643.MAXIMUM AVERAGE SUBARRAY I
def maximumAverageSubarrayI(nums,k):
    sums=sum(nums[:k])
    maxSums=sums
    for i in range(k,len(nums)):
        sums = sums-nums[i-k]+nums[i]
        maxSums=max(maxSums,sums)
    return maxSums/k
print(maximumAverageSubarrayI(nums=[1,12,-5,-6,50,3],k=4))

#3.LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
def longestSubstring(strs):
    s_unique=set()
    length=0
    maxLen=0
    for s in strs:
        if s not in s_unique:
            s_unique.add(s)
            length+=1
            maxLen=max(maxLen,length)
        else:
            s_unique.remove(s)
            length-=1
    return maxLen
print(longestSubstring("abcdefabcbbcdef"))

#or

def longestSubstringWithout(s):
    left,right=0,0
    s_char=set()
    maxLen=0
    while right<len(s):
        if s[right] not in s_char:
            s_char.add(s[right])
            maxLen=max(maxLen, right-left+1)
            right+=1
        else:
            s_char.remove(s[left])
            left+=1
    return maxLen
print(longestSubstringWithout("abcdabcbbd"))
            

#303.RANGE SUM QUERY - IMMUTABLE


#11.CONTAINER WITH MOST WATER
def containerWithMostWater(heights):
    l,r = 0,len(heights)-1
    area=0
    maxarea=0
    while l<r:
        length = min(heights[r],heights[l])
        breadth = r-l
        area=length*breadth
        maxarea=max(maxarea,area)
        if heights[r]>heights[l]:
            l+=1
        else:
            r-=1       
    return maxarea
print(containerWithMostWater(heights=[1,8,6,2,5,4,8,3,7]))

#121.BEST TIME TO BUY AND SELL STOCK
def bestTimeToBuyAndSellStock(prices):
    maxprofit=0
    if not prices:
        return 0
    n=len(prices)
    for i in range(n-1):
        for j in range(i+1,n):
            if prices[j]>prices[i]:
                profit=prices[j]-prices[i]
                maxprofit=max(maxprofit,profit)
    return maxprofit
print(bestTimeToBuyAndSellStock([7,1,5,3,6,4]))

#or
def bestTime(prices):
    l,r=0,1
    maxprofit=0
    while r<len(prices):
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            maxprofit=max(maxprofit,profit)
        else:
            l=r
        r+=1
    return maxprofit
print(bestTime([7,1,5,3,6,4]))
        
        
#28.Find index of first occurence in the string
def firstOccurence(haystack,needle):
    return haystack.find(needle)
print(firstOccurence(haystack = "sadbutsad", needle = "but"))

#or

def firstOccurence(haystack,needle):
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1
print(firstOccurence(haystack = "sadbutsad", needle = "but"))
        
  
#303.Range sum query-immutable
class NumArray:
    def __init__(self,nums):
        self.nums=nums
    def rangeSumQuery(self,left,right):
        return sum(self.nums[left:right+1])
nums=[-2, 0, 3, -5, 2, -1]
sol = NumArray(nums)
print(sol.rangeSumQuery(2,5))

#or

class Solution:
    def __init__(self,nums):
        self.prefix_sum=[0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1]+num)
    def sumRange(self,left,right):
        return self.prefix_sum[right+1]-self.prefix_sum[left]
sol = Solution([-2, 0, 3, -5, 2, -1])
print(sol.sumRange(0,2))
        

#21/8/2026

#268.MISSING NUMBER
def missingNumber(nums:list[int])->int:
    for i in range(len(nums)):
        if i in nums:
            i+=1
        else:
            return i
print(missingNumber(nums = [3,0,1]))


#3Sum
def threeSum(nums):
    n=len(nums)
    res=[]
    nums.sort()
    for i in range(n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        j,k = i+1,n-1
        while j<k:
            total=nums[i]+nums[j]+nums[k]
            if total==0:
                res.append([nums[i],nums[j],nums[k]])
                j+=1
                k-=1
                while j<k or nums[j]==nums[j-1]:
                    j+=1
                while j<k or nums[k]==nums[k+1]:
                    k-=1
            elif total<0:
                j+=1
            else:
                k-=1
    return res
print(threeSum([-1,0,-1,2,-1,-4]))
                    
       
#16.3 Sum Closest    
def closestSum(nums,target):
    n=len(nums)
    nums.sort()
    closest_sum=float('inf')
    for i in range(n-2):
        j,k=i+1,n-1
        while j<k:
            current_sum=nums[i]+nums[j]+nums[k]
            if abs(target-current_sum)<abs(target-closest_sum):
                closest_sum=current_sum
            if current_sum==target:
                return current_sum
            elif current_sum<target:
                j+=1
            else:
                k-=1
    return closest_sum
print(closestSum([-1,2,1,-4],1))
print(closestSum(nums = [0,0,0], target = 1))

                             
#18.4 Sum 
def fourSum(nums,target):
    nums.sort()
    n=len(nums)
    res=[]
    for a in range(n-3):
        if a>0 and nums[a]==nums[a-1]:
                continue
        for b in range(a+1,n-2):
            if b>0 and nums[b]==nums[b-1]:
                continue
            c,d=b+1,n-1
            while c<d:
                total=nums[a]+nums[b]+nums[c]+nums[d]
                if total==target:
                    res.append([nums[a],nums[b],nums[c],nums[d]])   
                    c+=1
                    d-=1
                    while c<d and nums[c]==nums[c-1]:
                        c+=1
                    while c<d and nums[d]==nums[d+1]:
                        d-=1
                elif total<target:
                    c+=1
                else:
                    d-=1
    return res
print(fourSum([1,0,-1,0,-2,2],0))          
                    

#23/8/26

#205.Isomorphic String
def isomorphicString(s,t):
    if len(s)!=len(t):
        return False
    map_s_to_t={}
    map_t_to_s={}
    for char_s,char_t in zip(s,t):
        if char_s in map_s_to_t:
            if map_s_to_t[char_s]!=char_t:
                return False
        else:
            if char_t in map_t_to_s:
                return False
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s
    return True
print(isomorphicString("paper","title"))


#290.Word Pattern
def wordPattern(pattern,s):
    map_p_to_s={}
    map_s_to_p={}
    s_word=s.split()
    if len(pattern)!=len(s_word):
        return False
    for char,word in zip(pattern,s_word):
        if char in map_p_to_s:
            if map_p_to_s[char]!=word:
                return False
        else:
            if word in map_s_to_p:
                return False
            map_p_to_s[char]=word
            map_s_to_p[word]=char
    return True
print(wordPattern("abba","dog cat cat dog"))


#415.ADD INTEGERS
def addIntegers(num1,num2):
    i = len(num1)-1
    j = len(num2)-1
    carry = 0
    res = []
    while i>=0 or j>=0 or carry:
        digit1 = int(num1[i]) if i>=0 else 0
        digit2 = int(num2[j]) if j>=0 else 0
        total = digit1 + digit2 + carry
        carry = total//10
        res.append(str(total%10))
        i-=1
        j-=1
    return ''.join(reversed(res))
print(addIntegers(num1="11",num2="123"))


#344.REVERSE STRING
def reverseString(s):
    left,right = 0,len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s
print(reverseString(s=["h","e","l","l","o"]))


#345.REVERSE VOWELS OF A STRING
def reverseVowels(s):
    vowels = "aeiouAEIOU"
    s=list(s)
    left,right = 0,len(s)-1
    while left<right:
        if s[left] in vowels:
            if s[right] in vowels:
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1
            else:
                right-=1
        else:
            left+=1
    return "".join(s)
print(reverseVowels("LeEtcOde"))
            
"""    
***MISTAKE
Since strings are immutable we need to convert the string to a list first in order to allow changing the individual characters of a string. 
After swapping convert it ack to a string, join functio will do it."""


#917.REVERSE ONLY LETTERS
def reverseLetters(s):
    s=list(s)
    left,right=0,len(s)-1
    while left<right:
        if s[left].isalpha() and s[right].isalpha():
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        if not s[left].isalpha():
            left+=1
        if not s[right].isalpha():
            right-=1
    return "".join(s)
print(reverseLetters("a-bC-dEf-ghIj!"))


#88.MERGE SORTED ARRAY
# def mergeSortedArray(nums1,m,nums2,n):
#     for i in range(m):
#         for j in range(n):
#             if nums2[j]<nums1[i]:
#                 nums1[i+1].insert(nums2[j])
#                 j+=1
#             else:
#                 i+=1
#     return nums1
# print(mergeSortedArray(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
                

#118.Pascal's Triangle



#566.RESHAPE THE MATRIX
def reshapeMatrix(mat,r,c):
    m,n = len(mat),len(mat[0])
    if r*c != m*n:
        return mat    
    new_mat=[]
    elements=[]
    for row in mat:
        for value in row:
            elements.append(value)
    for i in range(r):
        new_mat.append(elements[i*c:(i+1)*c])
    return new_mat
print(reshapeMatrix(mat = [[1,2],[3,4]], r = 1, c = 4))
print(reshapeMatrix(mat = [[1,2],[3,4]], r = 2, c = 4))
                
            
#867.TRANPOSE MATRIX
def transpose(mat):
    transpose = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return transpose
print(transpose([[2,4,-1],[-10,5,11],[18,-7,6]]))


#1572.MATRIX DIAGONAL SUM   
def diagonalSum(mat):
    res=0
    n = len(mat)
    for i in range(n):
        res+=mat[i][i]
        if i!=n-i-1:
            res+=mat[i][n-i-1]
    return res
print(diagonalSum(mat = [[1,2,3],[4,5,6],[7,8,9]]))

#1351.COUNT NEGATIVE NUMBBERS IN A SORTED MATRIX
def countNegatives(mat):
    count=0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]<0:
                count+=1
    return count
print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))

#766.TEOPLITZ MATRIX
def teoplitz(mat):
    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if mat[i][j] != mat[i-1][j-1]:
                return False
    return True
print(teoplitz([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))

#SEARCH IN A 2D MATRIX   
def searchMatrix(mat,target):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==target:
                return True
    return False
print(searchMatrix(mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 60))


#73.SET MATRIX ZEROES
def matrixZeroes(mat):
    if not mat or not mat[0]:
        return 
    zero_row,zero_col=set(),set()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==0:
                zero_row.add(i)
                zero_col.add(j)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i in zero_row or j in zero_col:
                mat[i][j]=0
    return mat
print(matrixZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
                
  
#463.ISLAND PERIMETER
def islandPerimeter(grid):
    if not grid or not grid[0]:
        return 0
    perimeter=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                perimeter+=4 
                if i>0 and grid[i-1][j]==1:
                    perimeter-=1
                if i<len(grid)-1 and grid[i+1][j]==1:
                    perimeter-=1
                if j>0 and grid[i][j-1]==1:
                    perimeter-=1
                if j<len(grid[0])-1 and grid[i][j+1]==1:
                    perimeter-=1
    return perimeter
print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))


#48.ROTATE IMAGE
def rotateImage(mat):
    transpose = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    for row in transpose:
        row.reverse()
    return transpose
print(rotateImage([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

#54.SPIRAL MATRIX
def spiral(matrix):
    top,bottom = 0, len(matrix)-1
    left,right = 0, len(matrix[0])-1
    res=[]
    while top<=bottom and left<=right:
        for j in range(left,right+1):
            res.append(matrix[top][j])
        top+=1
        for i in range(top,bottom+1):
            res.append(matrix[i][right])
        right-=1
        if top<=bottom:
            for j in range(right,left-1,-1):
                res.append(matrix[bottom][j])
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left+=1
    return res
print(spiral([[1,2,3],[4,5,6],[7,8,9]]))
        
    
#3446.SORT MATRIX BY DIAGONALS
def sortDiagonals(grid):
    n=len(grid)
    for i in range(n):
        tmp = [grid[i+j][j] for j in range(n-i)]
        tmp.sort(reverse=True)
        for j in range(n-i):
            grid[i+j][j]=tmp[j]
    for i in range(1,n):
        tmp = [grid[j][i+j] for j in range(n-i)]
        tmp.sort()
        for j in range(n-i):
            grid[j][i+j]=tmp[j]
    return grid
print(sortDiagonals(grid = [[1,7,3],[9,8,2],[4,5,6]]))                  
  
#25/6/2026

#Kth Element

#215.Kth Largest Element in an Array
import heapq
def kthLargest(nums,k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap,num)
    return min_heap[0]
print(kthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))

#or
def kthLargest(nums,k):
    return heapq.nlargest(k,nums)[-1]
print(kthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))


#347.TOP K FREQUENT ELEMENTS
import heapq
from collections import Counter
def top_k_frequent(nums,k):
    count=Counter(nums)
    return heapq.nlargest(k,count,key=count.get)
print(top_k_frequent(nums = [1,1,1,2,2,3], k = 2))

#or
def top_k_frequent(nums,k):
    freq = Counter(nums)
    heap=[]
    for num,count in freq.items():
        heapq.heappush(heap,(count,num))
        if len(heap)>k:
            heapq.heappop(heap)
    return [num for count,num in heap]
print(top_k_frequent(nums = [1,1,1,2,2,3], k = 2))


#973.K CLOSEST POINTS TO ORIGIN
def kClosestPoints(points,k):
    return heapq.nsmallest(k,points,lambda x:x[0]**2 + x[1]**2)
print(kClosestPoints(points = [[3,3],[5,-1],[-2,4]], k = 2))


#451.SORT CHARACTERS BY FREQUENCY
def sortCharacters(s):
    freq=Counter(s)
    max_heap = [(-freq,char) for char,freq in freq.items()]
    heapq.heapify(max_heap)
    res=[]
    while max_heap:
        freq,char=heapq.heappop(max_heap)
        res.append(char*(-freq))
    return ''.join(res)
print(sortCharacters("tree"))

#373.FIND K PAIRS WITH SMALLEST SUMS
def kPairs(nums1,nums2,k):
    res=[]
    for u in nums1:
        for v in nums2:
            res.append((u+v,u,v))
    res.sort()
    return [[u,v] for total,u,v in res[:k]]
print(kPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))


#378.Kth SMALLEST ELEMENT IN THE MATRIX
def smallestElement(matrix,k):
    n=len(matrix)
    heap=[(matrix[0][0],0,0)]
    visited=set((0,0))
    while k:
        val,r,c = heapq.heappop(heap)
        k-=1
        if k==0:
            return val        
        if r+1<n and (r+1,c) not in visited:
            heapq.heappush(heap,(matrix[r+1][c],r+1,c))
            visited.add((r+1,c))
        if c+1<n and (r,c+1) not in visited:
            heapq.heappush(heap,((matrix[r][c+1]),r,c+1))
            visited.add((r,c+1))
    return visited
print(smallestElement(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))   

#or 
def smallestElementMatrix(matrix,k):
    heap=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            heapq.heappush(heap,matrix[i][j])
    for _ in range(k-1):
        heapq.heappop(heap)
    return heapq.heappop(heap)
print(smallestElement(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))


#26/8/26

#Linked List

#206.REVERSE LINKED LIST
class LinkedList:
    def __init__(self,val):
        self.val=val
        self.next=None
        
def create_from_list(values):
    if not values:
        print("None")
    head=LinkedList(values[0])
    current=head
    for val in values[1:]:
        current.next=LinkedList(val)
        current=current.next
    return head
        
def print_ll(head):
    current=head
    while current:
        print(current.val,end="->")
        current=current.next
    print("None")
    
def reverse_ll(head):
    prev = None
    current = head
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    return prev
         
# N=int(input())
# values=list(map(int,input().split())) 
values=[1,2,3,4,5]
head=create_from_list((values))
head=reverse_ll((head))
print_ll(head)          


#876.MIDDLE OF THE LINKED LIST
class Linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def create_from_list(values):
    if not values:
        return None
    head = Linkedlist(values[0])
    current = head
    for val in values[1:]:
        current.next=Linkedlist(val)
        current=current.next
    return head

def print_ll(head):
    current=head
    while current:
        print(current.data,end="->")
        current=current.next
    print("None")
    
def middleNode(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

# values=list(map(int,input().split()))
values=[1,2,3,4,5]
head = create_from_list(values)
middle = middleNode(head)
print_ll(middle)
print(middle.data)


#141.LINKED LIST CYCLE
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def create_from_list(values):
    if not values:
        return None
    head=Node(values[0])
    current=head
    for val in values[1:]:
        current.next=Node(val)
        current=current.next
    if pos!=-1:
        cycle_node=head
        for _ in range(pos):
            cycle_node=cycle_node.next
        current.next=cycle_node
    return head
def ll_cycle_exists(head):
    pos=head
    tail=head
    while tail and tail.next:
        pos=pos.next
        tail=tail.next.next
        if pos==tail:
            return True
    return False
values=[3,2,0,-4]
pos=1
head=create_from_list(values)
# cycle=ll_cycle_exists(head)
# print_ll(cycle)
print(ll_cycle_exists(head))


#234.PALINDROME LINKED LIST
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def palindrome_ll(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    current=slow
    prev=None
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    first=head
    second=prev
    while second:
        if first.val!=second.val:
            return False
        first=first.next
        second=second.next
    return True
def create_from_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next=Node(val)
        current=current.next
    return head
values=[1,2,3,2,1]
head=create_from_list(values)
print(palindrome_ll(head))


#19.REMOVE NTH NODE FROM END OF LIST
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def removeNthNodeFromEnd(head,n):
    dummy=Node(0)
    dummy.next=head
    slow=dummy
    fast=dummy
    for _ in range(n+1):
        fast=fast.next
    while fast:
        slow=slow.next
        fast=fast.next
    slow.next=slow.next.next
    return dummy.next
def create_from_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next=Node(val)
        current=current.next
    return head
def print_ll(head):
    current=head
    while current:
        print(current.val,end="->")
        current=current.next
    print("None")
values=[1,2,3,4,5]
n=2
head=create_from_list(values)
print_ll(removeNthNodeFromEnd(head,n))

    
#21.MERGE TWO SORTED LISTS
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
# def mergesortedList(list1,list2):
#     res=[]
#     while list1 and list2:
#         if list1.val>list2.val:
#             res.append(list1.val)
#         else:
#             res.append(list2.val)
#     if list1:
#         res.append(list1.val)
#     if list2:
#         res.append(list2.val)
#     return res
def mergesortedlist(l1,l2):
    dummy=Node(None)
    head=dummy
    while l1 and l2:
        if l1.val<l2.val:
            head.next=l1
            l1=l1.next
        else:
            head.next=l2
            l2=l2.next
        head=head.next
    if l1:
        head.next=l1
    if l2:
        head.next=l2
    return dummy.next
def create_from_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next=Node(val)
        current=current.next
    return head
def print_ll(head):
    current=head
    while current:
        print(current.val,end="->")
        current=current.next
    print("None")
l1=create_from_list([1,2,4])
l2=create_from_list([1,3,4])
print_ll(mergesortedlist(l1,l2))

    
#2.ADD TWO NUMBERS
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def addTwoNumbers(l1,l2):
    dummy=Node(0)
    current=dummy
    carry=0
    while l1 or l2 or carry:
        val1=l1.val if l1 else 0
        val2=l2.val if l2 else 0
        total=val1+val2+carry
        carry=total//10
        current.next=Node(total%10)
        current=current.next
        if l1:
            l1=l1.next
        if l2:
            l2=l2.next
    return dummy.next
def create_from_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next=Node(val)
        current=current.next
    return head
def print_ll(head):
    res=[]
    while head:
        res.append(head.val)
        head=head.next
    print(res)
l1=create_from_list([2,4,3])
l2=create_from_list([5,6,4])    
print_ll(addTwoNumbers(l1,l2))
        

#83.REMOVE DUPLICATES FROM SORTED LIST
class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def removeDuplicates(head):
    current=head
    while current and current.next:
        if current.val==current.next.val:
            current.next=current.next.next
        else:
            current=current.next
    return head
def create_from_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next=Node(val)
        current=current.next
    return head
def print_ll(head):
    res=[]
    while head:
        res.append(str(head.val))
        head=head.next
    print("->".join(res))
values=[1,2,3,3,4,4,4,5]
head=create_from_list(values)
duplicates=removeDuplicates(head)
print_ll(duplicates)


#24.SWAP NODES IN PAIRS
class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def swapNodesInPairs(head):
    dummy=Node(0)
    dummy.next=head
    prev=dummy
    while head and head.next:
        first=head
        second=head.next
        prev.next=second
        first.next=second.next
        second.next=first
        prev=first
        head=first.next
    return dummy.next
def create_from_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next=Node(val)
        current=current.next
    return head  
def print_ll(head):
    res=[]
    while head:
        res.append(str(head.val))
        head=head.next
    print("->".join(res)) 
values=[1,3,5,6]
head=create_from_list(values)
print_ll(swapNodesInPairs(head))


#721.SWAPPING NODES IN A LINKED LIST
def swapNodes(head,k):
    slow=head
    fast=head
    for _ in range(k-1):
        fast=fast.next
    first_k_node=fast
    while fast.next:
        slow=slow.next
        fast=fast.next
    second_k_node=slow
    first_k_node.val,second_k_node.val=second_k_node.val,first_k_node.val
    return head
def create_from_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next=Node(val)
        current=current.next
    return head  
def print_ll(head):
    res=[]
    while head:
        res.append(str(head.val))
        head=head.next
    print("->".join(res)) 
values=[1,2,3,4,5]
k=2
head=create_from_list(values)
print_ll(swapNodes(head,k))
   
    
#27/8/26

#75.SORT COLORS
def sortColors(colors):
    n=len(colors)
    for i in range(n):
        for j in range(0,n-i-1):
            if colors[j]>colors[j+1]:
                colors[j],colors[j+1]=colors[j+1],colors[j]
    return colors
print(sortColors([0,2,1,0,2,1,2]))

#or - USING DUTCH NATIONAL FLAG ALGORITHM
def sortColor(nums):
    n=len(nums)
    low=0
    mid=0
    high=n-1
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else: #nums[mid]==2:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums
print(sortColor([1,0,1,2,1,1,2,1,0]))
        
            
#905. Sort Array By Parity
def sortArrayByParityI(nums):
    low,mid,high = 0,0,len(nums)-1
    while mid<=high:
        if nums[mid]%2==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]%2==1:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums
print(sortArrayByParityI([1,2,3,4,5,6]))


#922. Sort Array By Parity II
def sortArrayByParityII(nums):
    even,odd=0,1
    while even<len(nums) and odd<len(nums):
        while even<len(nums) and nums[even]%2==0:
            even+=2
        while odd<len(nums) and nums[odd]%2!=0:
            odd+=2
        if even<len(nums) and odd<len(nums):
            nums[even],nums[odd]=nums[odd],nums[even]
    return nums
print(sortArrayByParityII([4,2,5,7]))


#TREE

#94.BINARY TREE INORDER TRAVERSAL
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.right=TreeNode(4)
inorder(root)


#144.BINARY TREE PREORDER TRAVERSAL
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def preorder(root):
    res=[]
    def traversal(root):
        if root:
            traversal(root.left)
            res.append(str(root.val))
            traversal(root.right)
    traversal(root)
    print("->".join(res))
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.right=TreeNode(4)
preorder(root)
        
        
#145.BINARY TREE POSTORDER TRAVERSAL
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def postOrder(root):
    res=[]
    def traversal(root):
        if root:
            traversal(root.left)
            traversal(root.right)
            res.append(str(root.val))
    traversal(root)
    print("->".join(res))
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.right=TreeNode(4)
postOrder(root)


#104.MAXIMUM DEPTH OF BINARY TREE
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def maxDepth(root):
    if not root:
        return 0
    return 1+max(maxDepth(root.left),maxDepth(root.right))
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maxDepth(root))


#111.MINIMUM DEPTH OF BINARY TREE
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def minDepth(root):
    if not root:
        return 0
    if not root.left:
        return 1+minDepth(root.right)
    if not root.right:
        return 1+minDepth(root.left)
    return 1+min(minDepth(root.left),minDepth(root.right))
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(minDepth(root))
    
    
#102.BINARY TREE LEVEL ORDER TRAVERSAL448
from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def levelOrder(root):
    if not root:
        return []
    queue=deque([root])
    res=[]
    while queue:
        level_size=len(queue)
        level_node=[]
        for _ in range(level_size):
            node=queue.popleft()
            level_node.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level_node)
    return res
            
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrder(root))
 

#28/8/2026   

#700.SEARCH IN A BINARY SEARCH TREE
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def search(root,val):
    if not root:
        return None
    elif val==root.val:
        return root.val
    elif val<root.val:
        return search(root.left,val)
    else:  
        return search(root.right,val)
val=2
root=TreeNode(4)
root.left=TreeNode(2)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right=TreeNode(7)
res=search(root,val)
print(res)

        
#450.DELETE NODE IN A BINARY SEARCH TREE
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def delete(root,key):
    if not root:
        return None
    if key<root.val:
        root.left=delete(root.left,key)
    elif key>root.val:
        root.right=delete(root.right,key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        sucessor=findMin(root.right)
        root.val=sucessor.val
        root.right=delete(root.right,sucessor.val)
    return root
def findMin(node):
    while node.left:
        node=node.left
    return node
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
key=3
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
root=delete(root,key)
inorder(root)

print()


#701.INSERT INTO A BINARY SEARCH TREE
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def insertNode(root,val):
    if not root:
        return TreeNode(val)
    if val<root.val:
        root.left = insertNode(root.left,val)
    elif val>root.val:
        root.right = insertNode(root.right,val)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
root=TreeNode(4)
root.left=TreeNode(2)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right=TreeNode(7)
val=5
root=insertNode(root,val)
inorder(root)

print()

#872. Leaf-Similar Trees
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def leafSimilarTree(root1,root2):
    def leaves(root):
        if not root:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        return leaves(root.left)+leaves(root.right)
    return leaves(root1)==leaves(root2)
# Tree 1
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.right = TreeNode(9)
# Tree 2
root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(2)
root2.right.right = TreeNode(9)
# root2.right.right.left = TreeNode(10)
print(leafSimilarTree(root1,root2))


#1448. Count Good Nodes in Binary Tree
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def countGoodNodes(root):
    def dfs(node,maxVal):
        if not node:
            return 0
        count=0
        if node.val>=maxVal:
            count=1
            maxVal=node.val
        count+=dfs(node.left,maxVal)
        count+=dfs(node.right,maxVal)
        return count
    return dfs(root,root.val)
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
print(countGoodNodes(root))


#29/8/26

#110.BALANCED BINARY TREE
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def balancedTree(root):
    def dfs(node):
        if not node:
            return 0
        left=dfs(node.left)
        right=dfs(node.right)
        if abs(left-right)>1:
            return -1
        return 1+max(left,right)
    return dfs(root)!=-1
root1=TreeNode(3)
root1.left=TreeNode(9)
root1.right=TreeNode(20)
root1.right.left=TreeNode(15)
root1.right.right=TreeNode(7)
print(balancedTree(root1))


#543. Diameter of Binary Tree
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left 
        self.right=right
def diameterTree(root):
    diameter=0
    def dfs(node):
        nonlocal diameter 
        if not node:
            return 0
        left=dfs(node.left)
        right=dfs(node.right)
        diameter=max(diameter,left+right)
        return 1+max(left,right)
    dfs(root)
    return diameter
root1=TreeNode(1)
root1.left=TreeNode(2)
root1.left.left=TreeNode(4)
root1.left.right=TreeNode(5)
root1.right=TreeNode(3)
print(diameterTree(root1))
    
    
#98.VALIDATE BINARY SEARCH TREE    
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left 
        self.right=right
def validateBT(root):
    def dfs(node,low,high):
        if not node:
            return True
        if not low<node.val<high:
            return False
        return (dfs(node.left,low,node.val) and dfs(node.right,node.val,high))
    return dfs(root,float('-inf'),float('inf'))
root2=TreeNode(5)
root2.left=TreeNode(1)
root2.right=TreeNode(4)
root2.right.left=TreeNode(3)
root2.right.right=TreeNode(6)
print(validateBT(root2))


#236. Lowest Common Ancestor of a Binary Tree
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left 
        self.right=right
def lcaBT(root,p,q):
    def dfs(node):
        if not node:
            return None
        if node==p or node==q:
            return node
        left=dfs(node.left)
        right=dfs(node.right)
        if left and right:
            return node
        return left if left else right
    return dfs(root)
root1=TreeNode(3)
root1.left=TreeNode(5)
root1.left.left=TreeNode(6)
root1.left.right=TreeNode(2)
root1.left.right.left=TreeNode(7)
root1.left.right.right=TreeNode(4)
root1.right=TreeNode(1)
root1.right.left=TreeNode(0)
root1.right.right=TreeNode(8)
p = root1.left        # TreeNode with value 5
q = root1.right       # TreeNode with value 1
print(lcaBT(root1,p,q).val)


#235. Lowest Common Ancestor of a Binary Search Tree
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left 
        self.right=right
def lcaBST(root,p,q):
    curr=root
    while curr:
        if p.val<curr.val and q.val<curr.val:
            curr=curr.left
        elif p.val>curr.val and q.val>curr.val:
            curr=curr.right
        else:
            return curr
root1=TreeNode(6)
root1.left=TreeNode(2)
root1.left.left=TreeNode(0)
root1.left.right=TreeNode(4)
root1.left.right.left=TreeNode(3)
root1.left.right.right=TreeNode(5)
root1.right=TreeNode(8)
root1.right.right=TreeNode(9)
root1.right.left=TreeNode(7)
p = root1.left            # node with value 2
q = root1.left.right      # node with value 4
print(lcaBST(root,p,q).val)
        
       
#112.PATH SUM
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left 
        self.right=right
def pathSum(root,targetSum):
    def dfs(node,remaining):
        if not node:
            return False
        if not node.left and not node.right:
            return node.val==remaining
        return(
            dfs(node.left,remaining-node.val)
            or dfs(node.right,remaining-node.val)
        )
    return dfs(root,targetSum)
targetSum=22
root1=TreeNode(5)
root1.left=TreeNode(4)
root1.left.left=TreeNode(11)
root1.left.left.left=TreeNode(7)
root1.left.left.right=TreeNode(2)
root1.right=TreeNode(8)
root1.right.left=TreeNode(13)
root1.right.right=TreeNode(4)
root1.right.right.right=TreeNode(1)
print(pathSum(root1,targetSum))
        
        
#199.BINARY TREE RIGHT SIDE VIEW
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left 
        self.right=right
from collections import deque
def rightSideView(root):
    view=[]
    queue=deque([root])
    while queue:
        size=len(queue)
        for i in range(size):
            node=queue.popleft()
            if i==size-1:
                view.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return view
root1=TreeNode(1)
root1.left=TreeNode(2)
root1.right=TreeNode(3)
root1.left.right=TreeNode(5)
root1.right.right=TreeNode(4)
print(rightSideView(root1))
        

# 1161. Maximum Level Sum of a Binary Tree
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left 
        self.right=right
def maxLevelSum(root):
    if not root:
        return 0
    queue=deque([root])
    maxSum=float('-inf')
    maxLevel=1
    level=1
    while queue:
        size=len(queue)
        total=0
        for _ in range(size):
            node=queue.popleft()
            total+=node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if total>maxSum:
            maxSum=total
            maxLevel=level
        level+=1                
    return maxLevel
root1=TreeNode(1)
root1.left=TreeNode(7)
root1.right=TreeNode(0)
root1.left.left=TreeNode(7)
root1.left.right=TreeNode(-8)
print(maxLevelSum(root1))

 
#637. Average of Levels in Binary Tree
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left 
        self.right=right
def averageoflevels(root):
    if not root:
        return 0
    q=deque([root])
    avg=0
    res=[]
    level=0
    while q:
        size=len(q)
        total=0
        for _ in range(size):
            node=q.popleft()
            total+=node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        avg=total/size
        # maxAvg=max(maxAvg,avg)
        res.append(avg)
    level+=1
    return res
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
print(averageoflevels(root))
            
    

#515. Find Largest Value in Each Tree Row
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left 
        self.right=right
def largestValueRow(root):
    if not root:
        return 0
    res=[]
    q=deque([root])
    maxVal=float('-inf')
    level=1
    while q:
        size=len(q)
        for _ in range(size):
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node.val>maxVal:
                maxVal=node.val
        res.append(maxVal)
    level+=1
    return res
root=TreeNode(1)
root.left=TreeNode(3)
root.left.left=TreeNode(5)
root.left.right=TreeNode(3)
root.right=TreeNode(2)
root.right.right=TreeNode(9)
print(largestValueRow(root))


#30/8/2026

#GRAPH

#200.NUMBER OF ISLANDS
def numIslands(grid):
    if not grid:
        return 0
    def dfs(grid,r,c):
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]):
            return
        if grid[r][c]=="0":
            return
        grid[r][c]="0"
        dfs(grid,r+1,c)
        dfs(grid,r-1,c)
        dfs(grid,r,c+1)
        dfs(grid,r,c-1)
    count=0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]=="1":
                count+=1
                dfs(grid,r,c)
    return count
print(numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))


#733.FLOOD FILL
def floodFill(image,sr,sc,color):
    if not image:
        return []
    original=image[sr][sc]
    if original==color:
        return image
    def dfs(image,r,c):
        if r<0 or r>=len(image) or c<0 or c>=len(image[0]):
            return
        if image[r][c]!=original:
            return
        image[r][c]=color
        dfs(image,r-1,c)
        dfs(image,r+1,c)
        dfs(image,r,c-1)
        dfs(image,r,c+1)
    dfs(image,sr,sc)
    return image
print(floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))
            
            
#695. Max Area of Island
def maxAreaIslands(grid):
    if not grid:
        return 0
    maxArea=0
    def dfs(grid,r,c):
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]):
            return 0
        if grid[r][c]==0:
            return 0
        grid[r][c]=0
        return 1+dfs(grid,r-1,c)+dfs(grid,r+1,c)+dfs(grid,r,c-1)+dfs(grid,r,c+1)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]==1:
                area=dfs(grid,r,c)
                maxArea=max(maxArea,area)
    return maxArea
print(maxAreaIslands(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                             [0,0,0,0,0,0,0,1,1,1,0,0,0],
                             [0,1,1,0,1,0,0,0,0,0,0,0,0],
                             [0,1,0,0,1,1,0,0,1,0,1,0,0],
                             [0,1,0,0,1,1,0,0,1,1,1,0,0],
                             [0,0,0,0,0,0,0,0,0,0,1,0,0],
                             [0,0,0,0,0,0,0,1,1,1,0,0,0],
                             [0,0,0,0,0,0,0,1,1,0,0,0,0]]))

# 1/9/26

#GRAPH-Connected Components

#323. Number of Connected Components in an Undirected Graph
from collections import defaultdict
def conectedComponents(n,edges):
    graph=defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited=set()
    count=0
    def dfs(node):
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                dfs(nei)
    for node in range(n):
        if node not in visited:
            visited.add(node)
            dfs(node)
            count+=1
    return count
print(conectedComponents(n=6,edges=[[0,1], [1,2], [2,3], [4,5]]))


#547. Number of Provinces
def numProvinces(isConnected):
    n=len(isConnected)
    visited=set()
    provinces=0
    def dfs(node):
        for nei in range(n):
            if isConnected[node][nei]==1 and nei not in visited:
                visited.add(nei)
                dfs(nei)
    for node in range(n):
        if node not in visited:
            visited.add(node)
            dfs(node)
            provinces+=1
    return provinces
print(numProvinces(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))


#207. Course Schedule
def courseSchedule(numCourses,prerequisites):
    graph=defaultdict(list)
    indegree=[0]*numCourses
    for u,v in prerequisites:
        graph[u].append(v)
        indegree[v]+=1
    q=deque([i for i in range(numCourses) if indegree[i]==0])
    topo=[]
    while q:
        node=q.popleft()
        topo.append(node)
        for nei in graph[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                q.append(nei)
    if len(topo)!=numCourses:
        return False
    return True
print(courseSchedule(numCourses = 2, prerequisites = [[1,0]]))


#210. Course Schedule II
def courseScheduleII(numCourses,prerequisites):
    graph=defaultdict(list)
    indegree=[0]*numCourses
    for u,v in prerequisites:
        graph[v].append(u)
        indegree[u]+=1
    topo=[]
    q=deque([i for i in range(numCourses) if indegree[i]==0])
    while q:
        node=q.popleft()
        topo.append(node)
        for nei in graph[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                q.append(nei)
    if len(topo)!=numCourses:
        return []
    else:
        return topo
print(courseScheduleII(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))       
            

#1926:NEAREST EXIT FROM ENTRANCE IN MAZE      
def nearestExitMaze(maze,entrance):
    rows,cols=len(maze),len(maze[0])
    q=deque()
    q.append((entrance[0],entrance[1],0))
    maze[entrance[0]][entrance[1]]="+"
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        row,col,step=q.popleft()
        for dr,dc in directions:
            r,c=row+dr,col+dc
            if 0<=r<rows and 0<=c<cols and maze[r][c]==".":
                if r==0 or r==rows-1 or c==0 or c==cols-1:
                    return step+1
                maze[r][c]="+"
                q.append((r,c,step+1))
    return -1
print(nearestExitMaze(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]))


#994. Rotting Oranges
def rottingOranges(grid):
    fresh,time=0,0
    row,col=len(grid),len(grid[0])
    q=deque()
    for r in range(row):
        for c in range(col):
            if grid[r][c]==1:
                fresh+=1
            if grid[r][c]==2:
                q.append([r,c])
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    while q and fresh>0:
        for i in range(len(q)):
            r,c=q.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (nr<0 or nr==len(grid) or nc<0 or nc==len(grid[0]) or grid[nr][nc]!=1):
                    continue
                grid[nr][nc]=2
                q.append([nr,nc])
                fresh-=1
        time+=1
    return time if fresh==0 else -1
print(rottingOranges(grid = [[2,1,1],[1,1,0],[0,1,1]]))


#70.CLIMBING STAIRS
def climbingStairs(n):
    if n<=2:
        return n
    a,b=1,2
    for _ in range(3,n+1):
        a,b=b,a+b
    return b
print(climbingStairs(n=5))


#509.FIBINACCI NUMBER
def fib(n):
    if n<=1:
        return n
    a,b=0,1
    for _ in range(2,n+1):
        a,b=b,a+b
    return b
print(fib(n=10))


#322.COIN CHANGE    
def coinChange(coins,amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for i in range(1,amount+1):
        for coin in coins:
            if i-coin>=0:
                dp[i]=min(dp[i],dp[i-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1
print(coinChange(coins = [1,2,5], amount = 11))


#512.COIN CHANGE II
def coinChangeII(coins,amount):
    dp=[0]*(amount+1)
    dp[0]=1
    for coin in coins:
        for i in range(coin,amount+1):
            dp[i]+=dp[i-coin]
    return dp[amount]
print(coinChangeII(amount = 5, coins = [1,2,5]))


#91. Decode Ways
def decodeWays(s):
    n=len(s)
    dp=[0]*(n+1)
    dp[n]=1
    for i in range(n-1,-1,-1):
        if s[i]=="0":
            dp[i]=0
        else:
            dp[i]=dp[i+1]
            if (i+1<n and 10<=int(s[i:i+2])<=26):
                dp[i]+=dp[i+2]
    return dp[0]
print(decodeWays(s = "226"))


#494. Target Sum
def targetSum(nums,target):
    dp={}
    def backtrack(i,total):
        if i==len(nums):
            return 1 if total==target else 0
        if (i,total) in dp:
            return dp[(i,total)]
        dp[(i,total)]=(backtrack(i+1,total+nums[i])+backtrack(i+1,total-nums[i]))
        return dp[(i,total)]
    return backtrack(0,0)
print(targetSum(nums = [1,1,1,1,1], target = 3))
    

#62.UNIQUE PATHS
   