class Solution:
    def isHappy(self, n:int) -> bool:
        def get_next(number):
            while number>0:
                total_sum = 0 
                digit=number%10
                total_sum += digit*digit
                number//=10
            return total_sum
        
        slow = n
        fast = get_next(n)
        while fast!=1 and slow!=fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast==1
            
sol = Solution()
print(sol.isHappy(19))           