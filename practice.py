# #2sum

# def twoSum(arr,target):
#     left=0
#     right=len(arr)-1
#     while left<right:
#         s=arr[left]+arr[right]
#         if s==target:
#             return [left,right]
#         elif s<target:
#             left+=1
#         else:
#             right-=1
#     return 
   

# res=twoSum(arr=[2,7,11,15],target=9)
# print(res)
            
# #threesum
            
# def threeSum(nums):
#     n=len(nums)
#     nums.sort()
#     res=[]
#     for i in range(n):
#         if i>0 and nums[i]==nums[i-1]:
#             continue
#         j,k=i+1,n-1
#         while j<k:
#             total=nums[i]+nums[j]+nums[k]
#             if total==0:
#                 res.append((nums[i],nums[j],nums[k]))
#                 j+=1
#                 k-=1
#                 while j<k and nums[j]==nums[j-1]:
#                     j+=1
#                 while j<k and nums[k]==nums[k+1]:
#                     k-=1
#             elif total>0:
#                 k-=1
#             else:
#                 k+=1
#     return res
# out=threeSum([-1,0,1,2,-1,4])
# print(out)

# #3sumclosest

# def threeSumClosest(nums,target):
#     n=len(nums)
#     nums.sort()
#     closest=float('inf')
#     for i in range(n-2):
#         j,k=i+1,n-1
#         while j<k:
#             curr_sum=nums[i]+nums[j]+nums[k]
#             if abs(target-curr_sum)<abs(target-closest):
#                 closest=curr_sum
#             if curr_sum==target:
#                 return curr_sum
#             elif curr_sum<target:
#                 j+=1
#             else:
#                 k-=1
#     return closest
# res=threeSumClosest(nums = [-1,2,1,-4], target = 1)
# print(res)
                
# #4sum

# def fourSum(nums,target):
#     nums.sort()
#     n=len(nums)
#     res=[]
#     for i in range(n-3):
#         if i>0 and nums[i]==nums[i-1]:
#             continue
#         for j in range(i+1,n-2):
#             if j>=i+1 and nums[j]==nums[j-1]:
#                 continue
#             left,right=j+1,n-1
#             while left<right:
#                 total=nums[i]+nums[j]+nums[left]+nums[right]
#                 if total==target:
#                     res.append((nums[i],nums[j],nums[left],nums[right]))
#                     left+=1
#                     right-=1
#                     while left<right and nums[left]==nums[left-1]:
#                         left+=1
#                     while left<right and nums[right]==nums[right+1]:
#                         right-=1
#                 elif total<target:
#                     left+=1
#                 else:
#                     right-=1
#             return res
# res=fourSum(nums=[1,0,-1,0,-2,2],target=0)
# print(res)
                        
                        
                        



# def isPalidrome(s):
#     left,right=0,len(s)-1
#     while left<right:
#         while left<right and not s[left].isalnum():
#             left+=1
#         while left<right and not s[right].isalnum():
#             right-=1
#         if s[left].lower()!=s[right].lower():
#             return False
#         left+=1
#         right-=1
#     return True
# print(isPalidrome("A man, a plan, a canal: Panama"))

# def isPalindrome(s):
#     left,right = 0,len(s)-1
#     while left<right:
#         while left<right and not s[left].isalnum():
#             left+=1
#         while left<right and not s[right].isalnum():
#             right-=1
#         if s[left].lower()!=s[right].lower():
#             return False
#         left+=1
#         right-=1
#     return True            


# def validPalindromeII(s):
#     def isPalidrome(s,left,right):
#         while left<right:
#             if s[left]!=s[right]:
#                 return False
#             left+=1
#             right-=1
#         return True
#     left,right = 0,len(s)-1
#     while left<right:
#         if s[left]!=s[right]:
#             return isPalidrome(s,left+1,right) or isPalidrome(s,left,right-1)
#         left+=1
#         right-=1
#     return True
# print(validPalindromeII("abaca"))


# def validPalindromeII(s):

#     def isPalidrome(s,left,right):
#         while left<right:
#             if s[left]!=s[right]:
#                 return False
#             left+=1
#             right+=1
#         return True
#     left,right=0,len(s)-1
#     while left<right:
#         if s[left]!=s[right]:
#             return isPalidrome(s,left+1,right) or isPalidrome(s,left,right-1)
#         left+=1
#         right-=1
#     return True

        
                
# def decodeStrings(s):
#     n=len(s)
#     dp=[0]*(n+1)
#     dp[n]=1
#     for i in range(n-1,-1,-1):
#         if s[i]==0:
#             dp[i]=0
#         else:
#             dp[i]=dp[i+1]
#             if (i+1<n and 10<=int(s[i:i+2])<=26):
#                 dp[i]+=dp[i+2]
#     return dp[0]

# def decodestrings(s):
#     n=len(s)
#     dp=[0]*(n+1)
#     dp[n]=1
#     for i in range(n-1,-1,-1):
#         if s[i]=='0':
#             dp[i]=0
#         else:
#             dp[i]+=dp[i+1]
#             if (i+1<n and 10<=int(s[i:i+2])<=26):
#                 dp[i]+=dp[i+2]
#     return dp[0]
    
    
            
# def maxSubarray(nums,k):
#     window_sum=sum(nums[:k]) 
#     max_sum=window_sum
#     for i in range(k,len(nums)):
#         window_sum=window_sum-nums[i-k]+nums[i]
#         max_sum=max(max_sum,window_sum)
#     return max_sum/k        


# def maxAverageSubarray(nums,k):
#     window_sum=sum(nums[:k])
#     max_sum=window_sum
#     for i in range(k,len(nums)):
#         window_sum=window_sum-nums[i-k]+nums[i]
#         max_sum=max(max_sum,window_sum)
#     return max_sum/k



# def coinChange(coins,amount):
#     dp=[float('inf')]*(amount+1)
#     dp[0]=0
#     for i in range(1,amount+1):
#         for coin in coins:
#             if i-coin>=0:
#                 dp[i]=min(dp[i],1+dp[i-coin])
#     return dp[amount] if dp[amount]!=amount+1 else -1


# def coinChange(coins,amount):
#     dp=[float('inf')]*(amount+1)
#     dp[0]=0
#     for i in range(1,amount+1):
#         for coin in coins:
#             if i-coin>=0:
#                 dp[i]=min(dp[i],1+dp[i-coin])
#     return dp[amount] if dp[amount]!=float('inf') else -1


# def coinChnage(coins,amount):
#     dp=[float('inf')]*(amount+1)
#     dp[0]=0
#     for i in range(1,amount+1):
#         for coin in coins:
#             if i-coin>=0:
#                 dp[i]=min(dp[i],1+dp[i-coin])
#     return dp[amount] if dp[amount]!=float('inf') else -1
            
               
               
               
# def longSubstring(s):
#     left = 0
#     right = 0
#     maxlen = 0
#     char = set()
#     while right < len(s):
#         if s[right] not in char:
#             char.add(s[right])
#             maxlen = max(maxlen, right-left+1)
#             right+=1
#         else:
#             char.remove(s[left])
#             left+=1
#     return maxlen
# print(longSubstring("abcabcbb"))
            
            
            
# def longsubstring(s):
#     char=set()
#     left=0
#     right=0
#     maxlen=0
#     while right<len(s):
#         if s[right] not in char:
#             char.add(s[right])
#             maxlen=max(maxlen,right-left+1)
#             right+=1
#         else:
#             char.remove(s[left])
#             left+=1
#     return maxlen
# print(longsubstring("abcabcbb"))


class NumArray:
    def __init__(self, nums:list[int]):
        self.prefix_sum=[0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1]+num)
    def sumRange(self,left:int,right:int)->int:
        return self.prefix_sum[right+1]-self.prefix_sum[left]
sol=NumArray([-2,0,3,-5,2,-1])
print(sol.sumRange(0,2))

#-----------------explanation---------------

class NumArray:

    def __init__(self, nums: List[int]):
        
        # Create a prefix sum array and initialize it with 0.
        # prefix_sum[i] will store the sum of the first i elements.
        self.prefix_sum = [0]

        # Build the prefix sum array
        for num in nums:
            
            # self.prefix_sum[-1] gives the last prefix sum calculated
            # Add the current number to it and append the result
            self.prefix_sum.append(self.prefix_sum[-1] + num)

        # Example:
        # nums = [-2, 0, 3, -5, 2, -1]
        #
        # prefix_sum becomes:
        # [0, -2, -2, 1, -4, -2, -3]
        #
        # Meaning:
        # prefix_sum[0] = 0
        # prefix_sum[1] = -2
        # prefix_sum[2] = -2      (-2 + 0)
        # prefix_sum[3] = 1       (-2 + 0 + 3)
        # prefix_sum[4] = -4      (-2 + 0 + 3 - 5)
        # prefix_sum[5] = -2      (-2 + 0 + 3 - 5 + 2)
        # prefix_sum[6] = -3      (-2 + 0 + 3 - 5 + 2 - 1)


    def sumRange(self, left: int, right: int) -> int:

        # To find the sum from index left to right:
        #
        # prefix_sum[right + 1]
        # = sum of elements from index 0 to right
        #
        # prefix_sum[left]
        # = sum of elements before index left
        #
        # Subtracting them removes the unwanted part
        #
        # Formula:
        # Range Sum(left, right)
        # = prefix_sum[right + 1] - prefix_sum[left]

        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Example
sol = NumArray([-2, 0, 3, -5, 2, -1])

# sumRange(0, 2)
# = (-2 + 0 + 3)
# = 1
#
# prefix_sum[3] - prefix_sum[0]
# = 1 - 0
# = 1

print(sol.sumRange(0, 2))