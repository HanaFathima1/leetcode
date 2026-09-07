#7/9/2026

#BIT MANIPULATION

#136.SINGLE NUMBER
def singleNumber(nums):
    xor=0
    for num in nums:
        xor^=num
    return xor
print(singleNumber([1,2,3,1,4,5,3,5,2]))