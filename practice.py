#2sum

def twoSum(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        s=arr[left]+arr[right]
        if s==target:
            return [left,right]
        elif s<target:
            left+=1
        else:
            right-=1
    return 
   

res=twoSum(arr=[2,7,11,15],target=9)
print(res)
            
#threesum
            
def threeSum(nums):
    n=len(nums)
    nums.sort()
    res=[]
    for i in range(n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        j,k=i+1,n-1
        while j<k:
            total=nums[i]+nums[j]+nums[k]
            if total==0:
                res.append((nums[i],nums[j],nums[k]))
                j+=1
                k-=1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1
            elif total>0:
                k-=1
            else:
                k+=1
    return res
out=threeSum([-1,0,1,2,-1,4])
print(out)

#3sumclosest

def threeSumClosest(nums,target):
    n=len(nums)
    nums.sort()
    closest=float('inf')
    for i in range(n-2):
        j,k=i+1,n-1
        while j<k:
            curr_sum=nums[i]+nums[j]+nums[k]
            if abs(target-curr_sum)<abs(target-closest):
                closest=curr_sum
            if curr_sum==target:
                return curr_sum
            elif curr_sum<target:
                j+=1
            else:
                k-=1
    return closest
res=threeSumClosest(nums = [-1,2,1,-4], target = 1)
print(res)
                
#4sum

def fourSum(nums,target):
    nums.sort()
    n=len(nums)
    res=[]
    for i in range(n-3):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>=i+1 and nums[j]==nums[j-1]:
                continue
            left,right=j+1,n-1
            while left<right:
                total=nums[i]+nums[j]+nums[left]+nums[right]
                if total==target:
                    res.append((nums[i],nums[j],nums[left],nums[right]))
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif total<target:
                    left+=1
                else:
                    right-=1
            return res
res=fourSum(nums=[1,0,-1,0,-2,2],target=0)
print(res)
                        