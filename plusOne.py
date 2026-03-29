from typing import List

class Solution:
    def plusOne(self, digits:List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num+=1
        return list(map(int, str(num)))
    
sol = Solution()
print(sol.plusOne([1,2,3]))
print(sol.plusOne([9,9,9]))