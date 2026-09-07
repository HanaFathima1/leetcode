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


# class NumArray:
#     def __init__(self, nums:list[int]):
#         self.prefix_sum=[0]
#         for num in nums:
#             self.prefix_sum.append(self.prefix_sum[-1]+num)
#     def sumRange(self,left:int,right:int)->int:
#         return self.prefix_sum[right+1]-self.prefix_sum[left]
# sol=NumArray([-2,0,3,-5,2,-1])
# print(sol.sumRange(0,2))




# class NumArray:
#     def __init__(self, nums:list[int])->int:
#         self.prefix_sum=[0]
#         for num in nums:
#             self.prefix_sum.append(self.prefix_sum[-1]+num)
#     def sumRange(self,left:int,right:int)->int:
#         return self.prefix_sum[right+1]-self.prefix_sum[left]
# sol=NumArray()
# print(sol.sumRange())


# class NumArray:
#     def __init__(self,nums:list[int])->int:
#         self.prefix_sum=[0]
#         for num in nums:
#             self.prefix_sum.append(self.prefix_sum[-1]+num)
#     def sumRange(self,left:int,right:int)->int:
#         return self.prefix_sum[right+1]-self.prefix_sum[left]
# sol=NumArray()
# print(sol.sumRange())


# def miDistance(word1,word2):
#     m,n =len(word1),len(word2)
#     dp = [[0] * (n+1) for _ in range(m+1)]
#     for j in range(n+1):
#         dp[m][j]=n-j
#     for i in range(m+1):
#         dp[i][n]=m-i
#     for i in range(m-1,-1,-1):
#         for j in range(n-1,-1,-1):
#             if word1[i]==word2[j]:
#                 dp[i][j] = dp[i+1][j+1]
#             else:
#                 dp[i][j] = 1+min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
#     return dp[0][0]
# print(miDistance(word1 = "horse", word2 = "ros"))
        
        
# def nextGreater(nums1,nums2):
#     stack = []
#     next_greater = {}
#     for num in nums2:
#         while stack and num > stack[-1]:
#             smaller = stack.pop()
#             next_greater[smaller] = num
#         stack.append(num)
#     while stack:
#         next_greater[stack.pop()]=-1
#     return [next_greater[num] for num in nums1] 
# print(nextGreater([4,1,2],[1,3,4,2]))

# def nextGreater(nums1,nums2):
#     stack=[]
#     next_greater={}
#     for num in nums2:
#         while stack and num > stack[-1]:
#             smaller=stack.pop()
#             next_greater[smaller] = num
#         stack.append(num)
#     while stack:
#         next_greater[stack.pop()] = -1
#     return [next_greater[num] for num in nums1]


# def dailyTemp(temperatures):
#     stack = []
#     n=len(temperatures)
#     result = [0]*n
#     for i in range(n):
#         while stack and temperatures[i] > temperatures[stack[-1]]:
#             prev_index = stack.pop()
#             result[prev_index] = i - prev_index
#         stack.append(i)
#     return result
# print(dailyTemp(temperatures = [73,74,75,71,69,72,76,73]))


# def dailyTemp(temperatures):
#     n = len(temperatures)
#     result=[0]*n
#     stack=[]
#     for i in range(n):
#         while stack and temperatures[i] > temperatures[stack[-1]]:
#             prev_index = stack.pop()
#             result[prev_index] = i - prev_index
#         stack.append(i)
#     return result
# print(dailyTemp(temperatures = [73,74,75,71,69,72,76,73]))
    
    
# def nextgreater(nums1,nums2):
#     stack=[]
#     next_greater={}
#     for num in range(nums2):
#         while stack and nums2 > stack[-1]:
#             smaller = stack.pop()
#             next_greater[smaller]=num
#         stack.append(num)
#     while stack:
#         next_greater[stack.pop()]=-1
#     return [next_greater[num] for num in nums1]

# from collections import deque
# def dota(senate):
#     n = len(senate)
#     radiant=deque()
#     dire=deque()
#     for i in range(n):
#         if senate[i]=='R':
#             radiant.append(i)
#         else:
#             dire.append(i)
#     while radiant and dire:
#         r=radiant.popleft()
#         d=dire.popleft()
#         if r<d:
#             radiant.append(r+n)
#         else:
#             dire.append(d+n)
#     return "Radiant" if radiant else "Dire" 
# print(dota("RDRDDR"))

# def rotate(nums,k):
#     n=len(nums)
#     k=k%n
#     nums[:] = nums[n-k:] + nums[:n-k]
#     return nums
# print(rotate(nums = [1,2,3,4,5,6,7], k = 3))

# def container(heights):
#     n = len(heights)
#     left,right = 0,n-1
#     maxArea=0
#     while left < right:
#         width = right-left
#         area = width*max(heights[left],heights[right])
#         maxArea=max(maxArea,area)
#         if heights[left]<heights[right]:
#             left+=1
#         else:
#             right-=1
#     return maxArea
# print(container(heights = [1,8,6,2,5,4,8,3,7]))

# def conainer(height):
#     n=len(height)
#     left,right=0,n-1
#     maxarea=0
#     while left<right:
#         width=right-left
#         area=width*max(height[left],height[right])
#         maxarea=max(maxarea,area)
#         if height[left]<height[right]:
#             left+=1
#         else:
#             right-=1
#     return maxarea

  
# def bestTime(prices):
#     l,r = 0, 1
#     maxP=0
#     while r<len(prices):
#         if prices[l]<prices[r]:
#             profit=prices[r]-prices[l]
#             maxP=max(maxP,profit)  
#         else:
#             l=r
#         r+=1
#     return maxP
# print(bestTime([7,1,5,3,6,4]))

# def bestT(prices):
#     maxP=0
#     l,s=0,1
#     while s<len(prices):
#         if prices[l]<prices[s]:
#             profit=prices[s]-prices[l]
#             maxP=max(maxP,profit)
#         else:
#             l=s
#         s+=1
#     return maxP
# print(bestT([7,1,5,3,6,4]))
            
            
# def addBinary(a,b):
#     result = []
#     carry=0
#     i,j=len(a)-1,len(b)-1
#     while i>=0 or j>=0 or carry:
#         total = carry
#         if i>=0:
#             total+=int(a[i])
#             i-=1
#         if j>=0:
#             total+=int(b[j])
#             j-=1
#         result.append(str(total%2))
#         carry=total//2
#     return ' '.join(reversed(result))

# def addBinary(a,b):
#     result=0
#     i,j=len(a)-1,len(b)-1
#     carry=0
#     while i>=0 or j>=0 or carry:
#         total=carry
#         if i>=0:
#             total+=int(a[i])
#             i-=1
#         if j>=0:
#             total+=int(b[j])
#             j-=1
#         result.append(str(total%2))
#         carry=total//2
#     return ''.join(reversed(result))
    
            
      
# def convert(s,numRows):
#     if numRows==1:
#         return s
#     i=0
#     d=1
#     rows = [[] for _ in range(numRows)]
#     for char in s:
#         rows[i].append(char)
#         if i==0:
#             d=1
#         elif i==numRows-1:
#             d=-1
#         r+=d
#     ret=''
#     for i in range(numRows):
#         ret +''.join(rows[i])      
#     return ret


# def addDigits(nums):
#     while nums>=10:
#         sum_digits=0
#         while nums>0:
#             sum_digits+=nums%10
#             nums//=10
#         nums = sum_digits
#     return nums
# print(addDigits(538))

# def addDigits(num):
#     if num==0:
#         return 0
#     elif num%9==0:
#         return 9
#     return num%9
# print(addDigits(589))
            
     
# import heapq   
# def top_k_largest(nums,k):
#     min_heap = nums[:k]
#     heapq.heapify(min_heap)
#     for num in nums[k:]:
#         if num > min_heap[0]:
#             heapq.heappop(min_heap)
#             heapq.heappush(min_heap, num)
#     return min_heap
# print(top_k_largest([3,2,1,5,6,4],2))

# import heapq
# def kth_largest(nums,k):
#     return heapq.nlargest(k,nums)[-1]
# print(kth_largest([3,2,3,1,2,4,5,5,6],4))
# print(kth_largest([3,2,1,5,6,4],2))
    
    
# from collections import Counter
# import heapq
# def k_frequent(nums,k):
#     count = Counter(nums)
#     return heapq.nlargest(k, count.keys(), key=count.get)
# print(k_frequent([1,1,1,2,2,3],2))

# import heapq
# def k_closest(points,k):
#     return heapq.nsmallest(k,points,key=lambda x:x[0]**2 + x[1]**2)
# print(k_closest([[1,3],[-2,2]], k = 1))

# import heapq
# def kth_smallest_matrix(matrix,k):
#     n = len(matrix)
#     heap = [(matrix[0][0],0,0)]
#     visited = set((0,0))
#     while k:
#         val,r,c = heapq.heappop(heap)
#         k-=1
#         if k == 0:
#             return val
#         if r+1<n and (r+1,c) not in visited:
#             heapq.heappush(heap,(matrix[r+1][c],r+1,c))
#             visited.add((r+1,c))
#         if c+1<n and (r,c+1) not in visited:
#             heapq.heappush(heap,(matrix[r][c+1],r,c+1))
#             visited.add((r,c+1))
# print(kth_smallest_matrix([[1,5,9],[10,11,13],[12,13,15]], k = 8))


# import heapq
# def k_pairs(nums1,nums2,k):
#     if not nums1 or not nums2 or k==0:
#         return []
#     min_heap=[]
#     result=[]
#     for i in range(min(k,len(nums1))):
#         heapq.heappush(min_heap, (nums1[i]+nums2[0],i,0))
#     while min_heap and len(result)<k:
#         total,i,j=heapq.heappop(min_heap)
#         result.append([nums1[i],nums2[j]])
#         if j+1<len(nums2):
#             heapq.heappush(min_heap, (nums1[i]+nums2[j+1],i,j+1))
#     return result
# print(k_pairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))


# import heapq
# def k_pair(nums1,nums2,k):
#     if not nums1 or not nums2 or k==0:
#         return []
#     result=[]
#     min_heap=[]
#     for i in range(min(k,len(nums1))):
#         heapq.heappush(min_heap,(nums1[i]+nums2[0],i,0))
#     while min_heap and len(result)<k:
#         total,i,j=heapq.heappop(min_heap)
#         result.append((nums1[i],nums2[j]))
#         if j+1<len(nums2):
#             heapq.heappush(min_heap, (nums1[i]+nums2[j+1],i,j+1))
#     return result
# print(k_pair(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
        
   
     
# import heapq
# def k_pairs(nums1,nums2,k):
#     if not nums1 or not nums2 or k == 0:
#         return []
#     min_heap=[]
#     result=[]
#     for i in range(min(k,len(nums1))):
#         heapq.heappush(min_heap,(nums1[i]+nums2[0],i,0))
#     while min_heap and len(result)<k:
#         total,i,j=heapq.heappop(min_heap)
#         result.append((nums1[i],nums2[j]))
#         if j+1<len(nums2):
#             heapq.heappush(min_heap, (nums1[i]+nums2[j+1],i,j+1))
#     return result
# print(k_pairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
        
    
     

# def ipo(k,w,profits,capital):
#     projects=list(zip(capital,profits))
#     projects.sort()
#     max_heap=[]
#     i=0
#     n=len(projects)
#     for _ in range(k):
#         while i<n and projects[i][0]<=w:
#             heapq.heappush(max_heap, -projects[i][1])
#             i+=1
#         if not max_heap:
#             break
#         w+= -heapq.heappop(max_heap)
#     return w

# def ipo(w,k,profit,capital):
#     projects=list(zip(capital,profit))
#     projects.sort()
#     max_heap=[]
#     i=0
#     n=len(projects)
#     for _ in range(k):
#         while i<n and projects[i][0]<=w:
#             heapq.heappush(max_heap,-projects[i][1])
#             i+=1
#         if not max_heap:
#             break
#         w+= - heapq.heappop(max_heap)
#     return w



# def reshapeMatrix(mat,r,c):
#     m,n = len(mat), len(mat[0])
#     if m*n != r*c:
#         return mat
#     res = [[0]*c for _ in range(r)]
#     k = 0
#     for i in range(m):
#         for j in range(n):
#             res[k//c][k%c] = mat[i][j]
#             k+=1
#     return res
# print(reshapeMatrix([[1,2],[3,4]],1,4))


# def transpose(mat):
#     return [[mat[j][i] for j in range(len(mat[0]))] for i in range(len(mat))]
# print(transpose([[2,4,-1],[-10,5,11],[18,-7,6]]))
    
    
    
# def diagonalSum(mat):
#     n=len(mat)
#     total=0
#     for i in range(n):
#         total+=mat[i][i]
#         if i!=n-i-1:
#             total+=mat[i][n-i-1]
#     return total
# print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))




# def trailingZeroes(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     count=0
#     while fact%10==0:
#         count+=1
#         fact//=10
#     return count
# print(trailingZeroes(n=25))

# def trailingZero(n):
#     count=0
#     while n:
#         n//=5
#         count+=n
#     return count
# print(trailingZero(n=25))



# def rotateImage(matrix):
#     matrix=[[matrix[j][i] for j in range(len(matrix[0]))] for i in range(len(matrix))]
#     for row in matrix:
#         row.reverse()
#     return matrix
# print(rotateImage([[1,2,3],[4,5,6],[7,8,9]]))




# def validSudoku(board):
#     rows=[set() for _ in range(9)]
#     cols=[set() for _ in range(9)]
#     boxes=[set() for _ in range(9)]
#     for r in range(9):
#         for c in range(9):
#             val=board[r][c]
#             if val=='.':
#                 continue
#             box_index=(r//3)*3+(c//3)
#             if val in rows[r] or val in cols[c] or val in boxes[box_index]:
#                 return False
#             rows[r].add(val)
#             cols[c].add(val)
#             boxes[box_index].add(val)
#     return True
# print(validSudoku(board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))


# def maxPoints(points):
#     n=len(points)
#     if n<=2:
#         return n
#     answer=2
#     for i in range(n):
#         for j in range(i+1,n):
#             count=2
#             x1,y1=points[i]
#             x2,y2=points[j]
#             for k in range(n):
#                 if k==i or k==j:
#                     continue
#                 x3,y3=points[k]
#                 if (x2-x1)*(y3-y1)==(y2-y1)*(x3-x1):
#                     count+=1
#             answer=max(answer,count)
#     return answer
# print(maxPoints([[1,1],[2,2],[3,3]]))


# def cheapestFlight(n, flights, src, dst, k):
#     dist = [float('inf')] * n
#     dist[src] = 0
#     for _ in range(k+1):
#         temp = dist.copy()
#         for u,v,w in flights:
#             if dist[u]!=float('inf') and dist[u] + w < temp[v]:
#                 temp[v] = dist[u] + w
#         dist = temp
#     return -1 if dist[dst]!=float('inf') else dist[dst]


# def containerWithMostWater(height):
#     i,j = 0,len(height)-1
#     length,breadth = 0,0
#     maxArea=0
#     while i<j:
#         length = min(height[i], height[j])
#         breadth = j-1
#         area = length*breadth
#         maxArea = max(area, maxArea)
#         if height[i]>height[j]:
#             j-=1
#         else:
#             i+=1
#     return maxArea
# print(containerWithMostWater(height=[1,8,6,2,5,4,8,3,7]))


# def trap(heights):
#     l,r = 0,len(heights)-1
#     leftMax, rightMax = heights[l], heights[r]
#     res=0
#     if not heights:
#         return 0
#     while l<r:
#         if leftMax<rightMax:
#             l+=1
#             leftMax=max(leftMax, heights[l])
#             res+=(leftMax-heights[l])
#         else:
#             r-=1
#             rightMax=max(rightMax,heights[r])
#             res+=(rightMax-heights[r])
#     return res
# print(trap(heights=[0,1,0,2,1,0,1,3,2,1,2,1]))


# def validPlaindrome(s):
#     left, right = 0, len(s)-1
#     while left<right:
#         while left<right and not s[left].isalpha():
#             left+=1
#         while left<right and not s[right].isalpha():
#             right-=1
#         if s[left].lower() != s[right].lower():
#             return False
#         left+=1
#         right-=1
#     return True
# print(validPlaindrome(s = "A man, a plan, a canal: Panama"))
# print(validPlaindrome(s = "race a car"))

        
        
# def validPalindrome(s):
#     left=0
#     right = len(s)-1
#     while left<right:
#         while left<right and not left[s].isalnum():
#             left+=1
#         while left<right and not right[s].isalnum():
#             right-=1
#         if s[left]!=s[right]:
#             return False
#         left+=1
#         right-=1
#     return True
# print(validPlaindrome(s = "A man, a plan, a canal: Panama"))
# print(validPlaindrome(s = "race a car"))


# def validPalindromeII(s):
#     def isPalidrome(left,right):
#         while left<right:
#             if s[left]==s[right]:
#                 left+=1
#                 right-=1
#             elif s[left]!=s[right]:
#                 return False
#         return True
#     left,right=0,len(s)-1
#     while left<right:
#         if s[left]!=s[right]:
#             return isPalidrome(left+1,right) or isPalidrome(left,right-1)
#         left+=1
#         right-=1
#     return True
# print(validPalindromeII(s = "aba"))
# print(validPalindromeII(s = "abca"))
# print(validPalindromeII(s = "abc"))


# def romanToInteger(s):
#     total=0
#     roman={
#         "I":1,
#         "V":5,
#         "X":10,
#         "L":50,
#         "C":100,
#         "D":500,
#         "M":1000
#     }
#     for i in range(len(s)):
#         if i<len(s)-1 and roman[s[i]]<roman[s[i+1]]:
#             total-=roman[s[i]]
#         else:
#             total+=roman[s[i]]
#     return total            
# print(romanToInteger(s="MCMXCIV"))
            
        
# def integerToRoman(number):
#     integer=[
#         (1000,'M'),
#         (900,'CM'),
#         (500,'D'),
#         (400,'CD'),
#         (100,'C'),
#         (90,'XC'),
#         (50,'L'),
#         (40,'XL'),
#         (10,'X'),
#         (9,'IX'),
#         (5,'V'),
#         (4,'IV'),
#         (1,'I')
#     ]
#     result=""
#     for num,roman in integer:
#         while number>=num:
#             result+=roman
#             number-=num
#     return result
# print(integerToRoman(1994))


# def longestCommonPrefix(strs):
#     if not strs:
#         return ""
#     base=strs[0]
#     for i in range(len(base)):
#         for word in strs[1:]:
#             if i==len(word) or base[i]!=word[i]:
#                 return base[0:i]
#     return base
# print(longestCommonPrefix(strs = ["flower","flow","flight"]))
    


# def moveZeroes(arr):
#     i,j = 0,0
#     for j in range(len(arr)):
#         if arr[j]!=0:
#             arr[i],arr[j]=arr[j],arr[i]
#             i+=1
#             j+=1
#         else:
#             j+=1
#     return arr
# print(moveZeroes([0,1,0,3,12,0]))
        
            
# def removeDuplicates(nums):
#     i,j=0,1
#     for j in range(len(nums)):
#         if nums[i]!=nums[j]:
#             i+=1
#             nums[i]=nums[j]
#     return len(nums[:i+1])
# print(removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))



# def removeElement(nums, val):
#     i,j=0,0
#     for j in range(len(nums)):
#         if nums[j]!=val:
#             nums[i]=nums[j]
#             i+=1
#     return nums[:i]
# print(removeElement(nums = [0,1,2,2,3,0,4,2],val = 2))
    
    
# def maxAverageSubarray(nums,k):
#     window_sum=sum(nums[:k])
#     max_sum=0
#     for i in range(k,len(nums)):
#         window_sum=window_sum-nums[i-k]+nums[i]
#         max_sum=max(max_sum,window_sum)
#     return max_sum/k
# print(maxAverageSubarray([1,12,-5,-6,50,3],k=4))


# def longestSubstring(s):
#     left,right=0,0
#     char_set=set()
#     max_len=0
#     while right<len(s):
#         if s[right] not in char_set:
#             char_set.add(s[right])
#             max_len=max(max_len, right-left+1)
#             right+=1
#         else:
#             char_set.remove(s[right])
#             left+=1
#     return max_len
# print(longestSubstring(s="abcabcbbc"))
                
 
 
# def consecutiveOnes(nums):     
#     l,r = 0,0
#     maxlen=0
#     for r in range(len(nums)): 
#         if nums[r]==1:
#             r+=1
#             maxlen=max(maxlen,r-l)
#         else:
#             r+=1
#             l=r
#     return maxlen
# print(consecutiveOnes(nums=[1,1,0,1,1,1]))
# print(consecutiveOnes(nums=[1,0,1,1,0,1]))
            
            

# def kadanes(nums):
#     curr_max=nums[0]
#     global_max=nums[0]
#     for i in range(1,len(nums)):
#         curr_max=max(nums[i], curr_max+nums[i])
#         global_max=max(global_max,curr_max)
#     return global_max
# print(kadanes(nums=[-2,1,-3,4,-1,2,1,-5,4]))



# class NumArray:
#     def __init__(self,nums:list[int]):
#         self.prefix_sum=[0]
#         for num in nums:
#             self.prefix_sum.append(self.prefix_sum[-1]+num)
#     def rangeSum(self,left:int,right:int)->int:
#         return self.prefix_sum[right+1]-self.prefix_sum[left]
# sol=NumArray([-2,0,3,-5,2,-1])
# print(sol.rangeSum(0,2))
        
                
# def rangeSum(nums):
#     prefix=[0]*len(nums)
#     prefix[0]=nums[0]
#     for i in range(1,len(nums)):
#         prefix[i]=prefix[i-1]+nums[i]
#     print(prefix)
#     left,right=0,2 
#     if left==0:
#         return prefix[right]
#     else:
#         return prefix[right+1]-prefix[left]   
# print(rangeSum([-2,0,3,-5,2,-1]))  

 
 
# def twoSum(nums,target):
#     hashmap={}
#     for i,num in enumerate(nums):
#         complement = target-num
#         if complement not in hashmap:
#             hashmap[num]=i
#         else:
#             return [hashmap[complement],i]
#     return hashmap[complement],num
# print(twoSum([2,7,11,5],9))


# def containDuplicates(nums):
#     res=[]
#     for i in range(len(nums)):
#         if nums[i] not in res:
#             res.append(nums[i])
#         else:
#             return True
#     return False
# print(containDuplicates([1,2,3,3]))


# def validAnagram(s,t):
#     s_freq={}
#     t_freq={}
#     for char in s:
#         if char in s_freq:
#             s_freq[char]+=1
#         else:
#             s_freq[char]=1
#     for char in t:
#         if char in t_freq:
#             t_freq[char]+=1
#         else:
#             t_freq[char]=1
#     return s_freq==t_freq
# print(validAnagram(s = "anagram", t = "nagaram"))
# print(validAnagram(s = "rat", t = "car"))


# def validAnagram(s,t):
#     s_freq={}
#     t_freq={}
#     for char in s:
#         if char in s_freq:
#             s_freq[char]+=1
#         else:
#             s_freq[char]=1
#     for char in t:
#         if char in t_freq:
#             t_freq[char]+=1
#         else:
#             t_freq[char]=1
#     return s_freq==t_freq
# print(validAnagram(s = "rat", t = "car"))
            

# from collections import defaultdict
# def groupAnagrams(strs):
#     groups=defaultdict(list)
#     for word in strs:
#         key = "".join(sorted(word))
#         groups[key].append(word)
#     return list(groups.values())
# print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))     



# def validParenthesis(s):
#     stack=[]
#     closeToOpen={"}":"{", "]":"[", ")":"("}
#     for bracket in s:
#         if bracket in closeToOpen:
#             if stack and stack[-1]==closeToOpen[bracket]:
#                 stack.pop()
#             else:
#                 return False
#         else:
#             stack.append(bracket)
        
#     return True if len(stack)==0 else False
# print(validParenthesis(s = "()[]{}"))
# print(validParenthesis(s = "([])"))
# print(validParenthesis( s = "(]"))




# def nextGreater(nums1,nums2):
#     n=len(nums2)
#     stack=[]
#     ans=[-1]*n  
#     for i in range(n):
#         while stack and nums2[i]>nums2[stack[-1]]:
#             ans[stack.pop()]=nums2[i]
#         stack.append(i)
#     nge={}
#     for i in range(n):
#         nge[nums2[i]]=ans[i]
#     result=[]
#     for num in nums1:
#         result.append(nge[num])
#     return result
# print(nextGreater(nums1 = [4,1,2], nums2 = [1,3,4,2]))


# def dailyTemperature(temperatures):
#     stack=[]
#     n=len(temperatures)
#     ans=[0]*n
#     for i in range(n):
#         while stack and temperatures[i]>temperatures[stack[-1]]:
#             idx=stack.pop()
#             ans[idx] = i-idx
#         stack.append(i)
#     return ans
# print(dailyTemperature([73,74,75,71,69,72,76,72]))
        
  

# from collections import deque
# class MyStack:
#     def __init__(self):
#         self.queue=deque()
#     def push(self,x):
#         self.queue.append(x)
#     def pop(self):
#         for i in range(len(self.queue)-1):
#             self.queue.append(self.queue.popleft())
#         return self.queue.popleft()
#     def top(self):
#         return self.queue[-1]
#     def empty(self):
#         return len(self.queue)==0
# sol=MyStack()
# sol.push(10)
# print(sol.empty())
# print(sol.pop())
# print(sol.empty())



# class MyQueue:
#     def __init__(self):
#         self.stack1=[]
#         self.stack2=[]
#     def push(self,x):
#         self.stack1.append(x)
#     def pop(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         return self.stack2.pop()
#     def peek(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         return self.stack2[-1]
#     def empty(self):
#         return len(self.stack1)==len(self.stack2)
# sol=MyQueue()
# sol.push(10)
# print(sol.peek())
# print(sol.pop())
# print(sol.empty())


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
        
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def build_from_ll(self,values):
#         if not values:
#             return None
#         self.head = Node(values[0])
#         current = self.head
#         for val in values[1:]:
#             current.next=Node(val)
#             current=current.next
#     def print_ll(self,head):
#         current=head
#         while current:
#             print(current.data,end="->")
#             current=current.next
#         print("None")
#     def reverse_ll(self,head):
#         prev=None
#         current=head
#         while current:
#             next_node=current.next
#             current.next=prev
#             prev=current
#             current=next_node
#         return prev

# ll = LinkedList()
# ll.build_from_ll([1,2,3,4,5])
# reversed_head=ll.reverse_ll(ll.head)
# ll.print_ll(reversed_head)
                
        
        
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def create_ll(self,values):
#         if not values:
#             return None
#         self.head=Node(values[0])
#         current=self.head
#         for val in values[1:]:
#             current.next=Node(val)
#             current=current.next
#         return self.head
#     def print_ll(self,head):
#         current=head
#         while current:
#             print(current.data,end="->")
#             current=current.next
#         print("None")
#     def middle(self,head):
#         slow=head
#         fast=head
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#         return slow
# ll=LinkedList()
# head=ll.create_ll([1,2,3,4,5,6])
# mid=ll.middle(head)
# ll.print_ll(mid)

                
# class ListNode:
#     def __init__(self,data=0,next=None):
#         self.data=data
#         self.next=next
# def mergeLL(l1,l2):
#     dummy=LinkedList()
#     tail=dummy
#     while l1 and l2:
#         if l1.data<l2.data:
#             tail.next=l1
#             l1=l1.next
#         else:
#             tail.next=l2
#             l2=l2.next
#         tail=tail.next
#         if l1:
#             tail.next=l1
#         if l2:
#             tail.next=l2
#     return dummy.next
# ll=ListNode()


# class LinkedList:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next
# class Solution:
#     def addTwoIntegers(self,l1,l2):
#         dummy=LinkedList(0)
#         current=dummy
#         carry=0
#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0 
#             val2 = l2.val if l2 else 0  
#             total=val1+val2+carry
#             carry=total//10
#             current.next=LinkedList(total%10)
#             current=current.next
#             if l1:
#                 l1=l1.next
#             if l2:
#                 l2=l2.next
#         return dummy.next
# def create_ll(values):
#     head=LinkedList(values[0])
#     current=head
#     for val in values[1:]:
#         current.next=LinkedList(val)
#         current=current.next
#     return head
    
# def print_ll(head):
#     result=[]
#     while head:
#         result.append(head.val)
#         head=head.next
#     print(result)

# if __name__=="__main__":
#     l1=create_ll([2,3,4])
#     l2=create_ll([5,6,4])
#     sol=Solution()
#     res=sol.addTwoIntegers(l1,l2)
#     print_ll(res)            
            
        
# class ListNode:
#     def  __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next

# class Solution:
#     def removeDupe(self,head):
#         current=head
#         while current and current.next:
#             if current.val == current.next.val:
#                 current.next=current.next.next
#             else:
#                 current=current.next
#         return head
# def build_ll(values):
#     if not values:
#         print("None")
#     head=ListNode(values[0])
#     current=head
#     for val in values[1:]:
#         current.next=ListNode(val)
#         current=current.next
#     return head
# def print_ll(head):
#     current=head
#     while current:
#         print(current.val,end="->")
#         current=current.next
#     print("None")
# if __name__=="__main__":
#     values=[1,2,3,4,5]
#     head=build_ll(values)
#     sol=Solution()
#     updated_head=sol.removeDupe(head)
#     print_ll(updated_head)        
                


# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next
# class Solution:
#     def removeNthNodeFromEnd(head,n):
#         dummy=ListNode(0)
#         dummy.next=head
#         slow=fast=dummy
#         for _ in range(n+1):
#             fast=fast.next
#         while fast:
#             slow=slow.next
#             fast=fast.next
#         slow.next=slow.next.next
#         return dummy.next


# class Solution:
#     def swapPairs(head):
#         dummy=ListNode(0)
#         dummy.next=head
#         prev=dummy
#         while head and head.next:
#             first=head
#             second=head.next
#             prev.next=second
#             first.next=second.next
#             second.next=first
#             prev=first
#             head=first.next
#         return dummy.next
            
        
        
# def swapNodes(head,k):
#     fast=head
#     for _ in range(k-1):
#         fast=fast.next
#     first_k_node=fast
#     slow=head
#     while fast.next:
#         slow=slow.next
#         fast=fast.next
#     last_k_node=slow
#     first_k_node.val,last_k_node.val=last_k_node.val,first_k_node.val
#     return head

    
        
# def binarySearch(array,x):
#     low,high = 0,len(array)-1
#     while low<=high:
#         mid = (low + high)//2
#         if array[mid]==x:
#             return mid
#         elif array[mid]<x:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# print(binarySearch([-1,0,3,5,9,12],9))


# def searchSortedArray(nums,target):
#     low,high= 0,len(nums)-1
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]==target:
#             return mid
#         if nums[low] <= nums[mid]:
#             if nums[low]<=target<nums[mid]:
#                 high=mid-1
#             else:
#                 low=mid+1
#         else:
#             if nums[mid]<target<=nums[high]:
#                 low=mid+1
#             else:
#                 high=mid-1
#     return -1
# print(searchSortedArray(nums = [4,5,6,7,0,1,2], target = 0))
# print(searchSortedArray(nums = [4,5,6,7,0,1,2], target = 7))


            
# def minRotatedSortedArray(nums):
#     low,high=0,len(nums)-1   
#     while low<high:
#         mid=(low+high)//2
#         if nums[mid]>nums[high]:
#             low=mid+1
#         else:
#             high=mid
#     return nums[low]
# print(minRotatedSortedArray([3,4,5,1,2]))
            

# import math
# def kokoEatigbanana(piles,h):
#     left,right=0,max(piles)
#     ans=right
#     while left<=right:
#         hours=0
#         mid=(left+right)//2
#         for pile in piles:
#             hours+=math.ceil(pile/mid)
#         if hours<=h:
#             ans=mid
#             right=mid-1
#         else:
#             left=mid+1
#     return ans
# print(kokoEatigbanana([3,6,7,11],8))


  
# def peakElement(nums):
#     low,high=0,len(nums)-1
#     while low<high:
#         mid=(low+high)//2
#         if nums[mid]>nums[mid+1]:
#             high=mid
#         else:
#             low=mid+1
#     return low
# print(peakElement([1,2,3,1]))
    
  
  
# class TreeNode:
#     def __init__(self,values,left=None,right=None):
#         self.values=values
#         self.left=None
#         self.right=None  

# class Solution:
#     def sameTree(self,p,q):
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         if p.values!=q.values:
#             return False
#         return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)

# p=TreeNode(1)
# p.left=TreeNode(2)
# p.right=TreeNode(3)

# q=TreeNode(1)
# q.left=TreeNode(2)
# q.right=TreeNode(3)

# sol=Solution()
# print(sol.sameTree(p,q))



# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
# class Solution:
#     def isSymmetric(self,root):
#         if not root:
#             return True
#         return self.isMirror(root.left,root.right)
#     def isMirror(self,t1,t2):
#         if not t1 and not t2:
#             return True
#         if not t1 or not t2:
#             return False
#         if t1.val!=t2.val:
#             return False
#         return self.isMirror(t1.left,t2.right) and self.isMirror(t1.right,t2.left)

# root=TreeNode(1)
# root.left=TreeNode(2)
# root.right=TreeNode(2)
# root.left.left=TreeNode(3)
# root.left.right=TreeNode(4)
# root.right.left=TreeNode(4)
# root.right.right=TreeNode(3)


# sol=Solution()
# print(sol.isSymmetric(root))

# #=============

# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
          
# class Solution:
#     def invertTree(self,root):
#         if not root:
#             return None
#         root.left,root.right=root.right,root.left
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         return root

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val,end=" ")
#         inorder(root.right)
        
# root=TreeNode(2)
# root.left=TreeNode(1)
# root.right=TreeNode(3)

# sol=Solution()
# root=sol.invertTree(root)
# inorder(root)
        
     
# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
# class Solution:         
#     def maxDepth(self,root):
#         if not root:
#             return 0
#         left_tree=self.maxDepth(root.left)
#         right_tree=self.maxDepth(root.right)
#         return 1+max(left_tree,right_tree)
# root=TreeNode(3)
# root.left=TreeNode(9)
# root.right=TreeNode(20)
# root.right.left=TreeNode(15)
# root.right.right=TreeNode(6)
# root.right.right.right=TreeNode(9)
# sol=Solution()
# print(sol.maxDepth(root))
        

# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
# class Solution:
#     def minDepth(self,root):
#         if not root:
#             return 0
#         if not root.left:
#             return 1+self.minDepth(root.right)
#         if not root.right:
#             return 1+self.minDepth(root.left)
#         return 1+min(self.minDepth(root.left),self.minDepth(root.right))
# root=TreeNode(3)
# root.left=TreeNode(9)
# root.right=TreeNode(20)
# root.right.left=TreeNode(15)
# root.right.right=TreeNode(6)
# root.right.right.right=TreeNode(6)
# sol=Solution()
# print(sol.minDepth(root))
        

# from collections import deque
# class Solution:
#     def levelOrder(self,root):
#         if not root:
#             return None
#         res=[]
#         queue=deque([root])
#         while queue:
#             node=queue.popleft()
#             res.append(node.val)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         return res
# root=TreeNode(3)
# root.left=TreeNode(9)
# root.right=TreeNode(20)
# root.right.left=TreeNode(15)
# root.right.right=TreeNode(6)
# root.right.right.right=TreeNode(6)
# sol=Solution()
# print(sol.levelOrder(root))
                
            
 
# class Solution:
#     def diameterOfBT(self,root):
#         diameter=0
#         def dfs(node):
#             nonlocal diameter  
#             if not node:
#                 return 0
#             left=dfs(node.left)
#             right=dfs(node.right)
#             diameter=max(diameter,left+right)
#             return 1+max(left,right)
#         dfs(root)
#         return diameter
# root=TreeNode(1)
# root.left=TreeNode(2)
# root.right=TreeNode(3)
# root.left.left=TreeNode(4)
# root.left.right=TreeNode(5)
# sol=Solution()
# print(sol.diameterOfBT(root))
            
    
# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
# class Solution:
#     def validateBST(self,root):
#         def dfs(node,low,high):
#             if not node:
#                 return True
#             if not low<node.val<high:
#                 return False
#             return (dfs(node.left,low,node.val) and dfs(node.right,node.val,high))
#         return dfs(root,float('-inf'),float('inf'))
# root=TreeNode(2)
# root.left=TreeNode(1)
# root.right=TreeNode(3)
# sol=Solution()
# print(sol.validateBST(root))
               
                
# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
# class Solution:
#     def searchBST(self,root,val):
#         if not root:
#             return None
#         elif val==root.val:
#             return root
#         elif val<root.val:
#             return self.searchBST(root.left,val)
#         else:
#             return self.searchBST(root.right,val)
# root=TreeNode(4)
# root.left=TreeNode(2)
# root.right=TreeNode(7)
# root.left.left=TreeNode(1)
# root.left.right=TreeNode(3)
# sol=Solution()
# result=sol.searchBST(root,2)
# print(result.val)


# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
# class Solution:
#     def lca(self,root,p,q):
#         def dfs(node):
#             if not node:
#                 return None
#             if node==p or node==q:
#                 return node
#             left=dfs(node.left)
#             right=dfs(node.right)
#             if left and right:
#                 return node
#             return left if left  else right
#         return dfs(root)
# root=TreeNode(3)
# root.left=TreeNode(5)
# root.right=TreeNode(1)
# root.left.left=TreeNode(6)
# root.left.right=TreeNode(2)
# root.left.right.left=TreeNode(7)
# root.left.right.right=TreeNode(4)
# root.right.left=TreeNode(0)
# root.right.right=TreeNode(8)
# p=root.left
# q=root.right
# sol=Solution()
# print(sol.lca(root,p,q).val)



# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
# class Solution:
#     def lcaBST(self,root,p,q):
#         curr=root
#         while curr:
#             if p.val<curr.val and q.val<curr.val:
#                 curr=curr.left
#             elif p.val>curr.val and q.val>curr.val:
#                 curr=curr.right
#             else:
#                 return curr
            
# root1=TreeNode(6)
# root1.left=TreeNode(2)
# root1.left.left=TreeNode(0)
# root1.left.right=TreeNode(4)
# root1.left.right.left=TreeNode(3)
# root1.left.right.right=TreeNode(5)
# root1.right=TreeNode(8)
# root1.right.right=TreeNode(9)
# root1.right.left=TreeNode(7)

# # p and q MUST be TreeNode references
# p = root1.left            # node with value 2
# q = root1.left.right      # node with value 4
# sol=Solution()
# print(sol.lcaBST(root,p,q).val)
            
            
            
# class Solution:
#     def pathSum(self,root,targetSum):
#         def dfs(node,remaining):
#             if not node:
#                 return 0
#             if node.val==remaining:
#                 return True
#             return(dfs(node.left,remaining-node.val)
#                    or
#                    (dfs(node.right,remaining-node.val)))
#         return dfs(root,targetSum)
# root1=TreeNode(5)
# root1.left=TreeNode(4)
# root1.left.left=TreeNode(11)
# root1.left.left.left=TreeNode(7)
# root1.left.left.right=TreeNode(2)
# root1.right=TreeNode(8)
# root1.right.left=TreeNode(13)
# root1.right.right=TreeNode(4)
# root1.right.right.right=TreeNode(1)
# sol=Solution()
# print(sol.pathSum(root1,targetSum=22))
                
    
    
# class Solution:
#     def rightSideView(self,root):
#         if not root:
#             return None
#         queue=deque([root])
#         view=[]
#         while queue:
#             size=len(queue)
#             for i in range(size):
#                 node=queue.popleft()
#                 if i==size-1:
#                     view.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return view
# root1=TreeNode(1)
# root1.left=TreeNode(2)
# root1.right=TreeNode(3)
# root1.left.right=TreeNode(5)
# root1.right.right=TreeNode(4)
# sol=Solution()
# print(sol.rightSideView(root1))
                    
                    

# class Solution:
#     def averageLevels(self,root):
#         if not root:
#             return []
#         queue=deque([root])
#         res=[]
#         avg=0
#         while queue:
#             size=len(queue)
#             total=0
#             for i in range(size):
#                     node=queue.popleft()
#                     total+=node.val
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#             avg=total/size
#             res.append(avg)
#         return res
# root=TreeNode(3)
# root.left=TreeNode(9)
# root.right=TreeNode(20)
# root.right.left=TreeNode(15)
# root.right.right=TreeNode(7)
# sol=Solution()
# print(sol.averageLevels(root))
            
                        
                        

# class Solution:
#     def largestValue(self,root):
#         if not root:
#             return None
#         res=[]
#         level=0
#         queue=deque([root])
#         while queue:
#             size=len(queue)
#             max_value=float('-inf')
#             for _ in range(size):
#                 node=queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#                 max_value=max(max_value,node.val)
#             res.append(max_value)
#             level+=1
#         return res
# root=TreeNode(1)
# root.left=TreeNode(3)
# root.left.left=TreeNode(5)
# root.left.right=TreeNode(3)
# root.right=TreeNode(2)
# root.right.right=TreeNode(9)
# sol=Solution()
# print(sol.largestValue(root))
            

# class Solution:
#     def numberOfIslands(self,grid):
#         if not grid:
#                 return 0
#         def dfs(grid,r,c):
#             row,col=len(grid),len(grid[0])
#             if r<0 or r>=row or c<0 or c>=col:
#                 return 
#             if grid[r][c]=="0":
#                 return 
#             grid[r][c]="0"
#             dfs(grid,r+1,c)
#             dfs(grid,r-1,c)
#             dfs(grid,r,c+1)
#             dfs(grid,r,c-1)
#         count=0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]=="1":
#                     count+=1
#                     dfs(grid,i,j)
#         return count
# sol=Solution()
# print(sol.numberOfIslands(grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]))     
# print(sol.numberOfIslands(grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]))



# class Solutiion:
#     def maxAreaIsland(self,grid):
#         if not grid: 
#             return 0
#         def dfs(grid,r,c):
#             row=len(grid)
#             col=len(grid[0])
#             if r<0 or r>=row or c<0 or c>=col or grid[r][c]==0:
#                 return 0
#             grid[r][c]=0
#             return (1+dfs(grid,r+1,c)+dfs(grid,r-1,c)+dfs(grid,r,c+1)+dfs(grid,r,c-1))
#         maxArea=0
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c]==1:
#                     maxArea=max(dfs(grid,r,c),maxArea)
#         return maxArea
# sol=Solutiion()
# print(sol.maxAreaIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#                                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
#                                 [0,1,1,0,1,0,0,0,0,0,0,0,0],
#                                 [0,1,0,0,1,1,0,0,1,0,1,0,0],
#                                 [0,1,0,0,1,1,0,0,1,1,1,0,0],
#                                 [0,0,0,0,0,0,0,0,0,0,1,0,0],
#                                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
#                                 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))



                    
# class Solution:
#     def rottingOranges(self,grid):
#         rows,cols=len(grid),len(grid[0])
#         fresh=0
#         time=0
#         queue=deque()
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c]==1:
#                     fresh+=1    
#                 if grid[r][c]==2:
#                     queue.append([r,c])
#         directions=[[1,0],[-1,0],[0,-1],[0,1]]
#         while queue and fresh>0:
#             for i in range(len(queue)):
#                 r,c=queue.popleft()
#                 for dr,dc in directions:
#                     nr,nc=r+dr,c+dc
#                     if nr<0 or nr==len(grid) or nc<0 or nc==len(grid[0]) or grid[nr][nc]!=1:
#                         continue
#                     grid[nr][nc]=2
#                     queue.append([nr,nc])
#                     fresh-=1
#             time+=1
#         return time if fresh==0 else -1
# sol=Solution()
# print(sol.rottingOranges(grid = [[2,1,1],[1,1,0],[0,1,1]]))



# def ShortestBinary(grid):
#     n=len(grid)
#     if grid[0][0]==1 or grid[n-1][n-1]==1:
#         return -1
#     queue=deque()
#     queue.append((0,0,1))
#     directions=[(1,0),(-1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]
#     while queue:
#         r,c,dist=queue.popleft()
#         if r==n-1 or c==n-1:
#             return dist
#         for dr,dc in directions:
#             nr,nc=r+dr,c+dc
#             if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0 and grid[nr][nc]==0:
#                 grid[nr][nc]=1
#                 queue.append((nr,nc,dist+1))
#     return -1
# print(ShortestBinary(grid = [[0,1],[1,0]]))
                

                
                           
                            
# class Solution:
#     def nearestMaze(maze,entrance):
#         row,col = len(maze),len(maze[0])
#         queue = deque()
#         queue.append(entrance[0],entrance[1],0)
#         maze[entrance[0][1]]="+"
#         directions=[(-1,0),(1,0),(0,-1),(0,1)]
#         while queue:
#             row,col,steps = queue.popleft()
#             for dr,dc in directions:
#                 nr,nc = row+dr, col+dc
#                 if 0<=nr<row or 0<=nc<col or maze[nr][nc]==".":
#                     if nr==0 or nr==row-1 or nc==0 or nc==col-1:
#                         return steps+1
#                     maze[nr][nc]="+"
#                     queue.append((nr,nc,steps+1))
#         return -1
    

# def floofFill(image,sr,sc,color):
#     row,col=len(image),len(image[0])
#     oldColor=image[sr][sc]
#     if oldColor == color:
#         return image
#     def dfs(r,c):
#         if r<0 or r>=row or c<0 or c>=col:
#             return
#         if image[r][c]!=oldColor:
#             return
#         image[sr][sc]=color
#         dfs(r+1,c)
#         dfs(r-1,c)
#         dfs(r,c+1)
#         dfs(r,c-1)
#     dfs(sr,sc)
#     return image


# import heapq
# from collections import defaultdict
# def dijkshtra(graph,V,start):
#     dist = [float('inf')]*V
#     dist[start] = 0
#     heap = [(0,start)]
#     while heap:
#         d,u = heapq.heappop(heap)
#         if d>dist[u]:
#             continue
#         for v,weight in graph[u]:
#             if dist[u]+weight<dist[v]:
#                 dist[v]=dist[u]+weight
#                 heapq.heappush(heap,(dist[v],v))
#     return dist
# graph=defaultdict(list)
# graph[0]=[(1,4),(2,1)]
# graph[1]=[(3,1)]
# graph[2]=[(1,2),(3,5)]
# graph[3]=[]
# V=4
# print(dijkshtra(graph,V,0))




# import heapq
# def networkTime(time,n,k):
#     graph=defaultdict(list)
#     for u,v,w in time:
#         graph[u].append((v,w))
#     dist=[float('inf')]*(n+1)
#     dist[k]=0
#     heap=[(0,k)]
#     while heap:
#         d,node = heapq.heappop(heap)
#         if d>dist[node]:
#             continue
#         for nei,wt in graph[node]:
#             if dist[node]+wt<dist[nei]:
#                 dist[nei]=dist[node]+wt
#                 heapq.heappush(heap,(dist[nei],nei))
#     max_time = max(dist[1:])
#     return -1 if max_time==float('inf') else max_time
# print(networkTime(time = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))



# def cheapestFlght(n,flights,src,dst,k):
#     dist=[float('inf')]*n
#     dist[src]=0
#     for _ in range(k+1):
#         temp=dist.copy()
#         for u,v,price in flights:
#             if dist[u]!=float('inf') and dist[u]+price<temp[v]:
#                 temp[v]=dist[u]+price
#         dist=temp
#     return -1 if dist[dst]==float('inf') else dist[dst]
# print(cheapestFlght(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
            
   
   
 
# def houseRobber(nums):
#     n = len(nums)
#     if n==1:
#         return nums[0]
#     dp=[0]*n
#     dp[0]=nums[0]
#     dp[1]=max(nums[0],nums[1])
#     for i in range(2,n):
#         dp[i]=max(nums[i]+dp[i-2],dp[i-1])
#     return dp[n-1]
# print(houseRobber(nums=[1,2,3,1]))      
# print(houseRobber(nums=[2,7,9,3,1]))        
            
 

# def coinChange(coins,amount):
#     dp=[float('inf')]*(amount+1)
#     dp[0]=0
#     for i in range(1,amount+1):
#         for coin in coins:
#             if i-coin>=0:
#                 dp[i]=min(dp[i],1+dp[i-coin])
#     return dp[amount] if dp[amount]!=float('inf') else -1
# print(coinChange(coins=[1,2,5],amount=11))
                    


# def uniquePaths(m,n):
#     dp=[[0]*n for _ in range(m)]
#     for i in range(m):
#         dp[0][i]=1
#     for j in range(n):
#         dp[i][0]=1
#     for i in range(1,m):
#         for j in range(1,n):
#             dp[i][j]=dp[i-1][j]+dp[i][j-1]
#     return dp[-1][-1]
# print(uniquePaths(m=3,n=4))



# def lcs(text1,text2):
#     m,n = len(text1),len(text2)
#     dp=[[0]*(n+1) for _ in range(m+1)]
#     for i in range(m-1,-1,-1):
#         for j in range(n-1,-1,-1):
#             if text1[i]==text2[j]:
#                 dp[i][j]=1+dp[i+1][j+1]
#             else:
#                 dp[i][j]=max(dp[i+1][j],dp[i][j+1])
#     return dp[0][0]
# print(lcs(text1="ace",text2="abhce"))
                
                


# def editDistance(word1,word2):
#     m,n = len(word1),len(word2)
#     dp=[[0]*(n+1) for _ in range(m+1)]
#     for j in range(n+1):
#         dp[m][j]=n-j
#     for i in range(m+1):
#         dp[i][n]=m-i
#     for i in range(m-1,-1,-1):
#         for j in range(n-1,-1,-1):
#             if word1[i]==word2[j]:
#                 dp[i][j]=dp[i+1][j+1]
#             else:
#                 dp[i][j]=1+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
#     return dp[0][0]
# print(editDistance(word1 = "horse", word2 = "ros"))
            
            
            
# def lis(nums):
#     n=len(nums)
#     dp=[1]*n
#     for i in range(n):
#         for j in range(i):
#             if nums[j]<nums[i]:
#                 dp[i]=max(dp[i],dp[j]+1)
#     return max(dp)
# print(lis(nums=[10,9,2,5,3,7,101,18]))



# def jumpGame(nums):
#     farthest=0
#     for i in range(len(nums)):
#         if i>farthest:
#             return False
#         else:
#             farthest=max(farthest,i+nums[i])
#     return True
# print(jumpGame(nums=[2,3,1,1,4]))



# def overlappingIntervals(intervals):
#     if not intervals:
#         return 0
#     intervals.sort(key=lambda x:x[1])
#     end=intervals[0][1]
#     remove=0
#     for s,e in intervals[1:]:
#         if s<end:
#             remove+=1
#         else:
#             end=e
#     return remove
# print(overlappingIntervals([[1,2],[1,3],[2,3]]))



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
            res-=roman[s[i]]
        else:
            res+=roman[s[i]]
    return res
print(romanToInt("MCMXCIV"))



def integerToRoman(num):
    res=""
    roman_map=[
        (1000,"M"),
        (900,"CM"),
        (500,"D"),
        (400,"CD"),
        (100,"C"),
        (90,"XC"),
        (50,"L"),
        (40,"XL"),
        (10,"X"),
        (9,"IX"),
        (5,"V"),
        (4,"IV"),
        (1,"I")
    ] 
    for digit,symbol in roman_map:
        while num>=digit:
            res+=symbol
            num-=digit
    return res
print(integerToRoman(1994))
                   
        
        