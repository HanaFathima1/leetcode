class NumArray: 
    def __init__(self, nums:list[int]):
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1]+num)
    def sumRange(self, left:int, right:int) -> int:
        return self.prefix_sum[right+1]-self.prefix_sum[left]
sol = NumArray([-2,0,3,-5,2,-1])
print(sol.sumRange(0,2))
