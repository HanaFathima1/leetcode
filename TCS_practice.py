#===============TCS NQT PREPARATION=================

#=====print even or odd=========
def oddeven(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
print(oddeven(num=120))    

#==========check prime number================
def countPrime(n):
    if n<=2:
        return 0
    is_prime=[True]*n
    is_prime[0]=is_prime[1]=False
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i,n,i):
                is_prime[j]=False
    return sum(is_prime)
print(countPrime(10))
    
#==========check prime number=============
def isPrime(num):
    if num<2:
        return "Not Prime"
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return "Not prime"
        return "Prime"
print(isPrime(6))

#============factorial============
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
print(factorial(3))

#============fibonacci=========
def fibonacci(num):
    # if num<1:
    #     return num
    a,b=0,1
    for _ in range(num):
        print(a,end=" ")
        a,b = b,a+b
    # return b
print(fibonacci(24))

#============reverse a number=========
def reverse(n):
    rev=0
    while n>0:
        digit = n%10
        rev = rev*10 + digit
        n//=10
    return rev
print(reverse(134))

#============palindrome check=========
def palidrome(n):
    return (str(n) == str(n)[::-1])
print(palidrome(323))

#or 
def palindrom(n):
    original = n
    rev = 0
    while n>0:
        digit = n%10
        rev=rev*10+digit
        n//=10
    if original == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(palindrom(43534))

#==========armstrong=========
def armstrong(num):
    number = num
    n = len(str(num))
    total = 0
    while num>0:
        digit = num%10
        total += digit**n
        num//=10
    return "True" if total == number else "False"
print(armstrong(153))
        

#=============sum of digits============
def sum_digits(num):
    total = 0 
    while num>0:
        digit=num%10
        total+=digit
        num//=10
    return total
print(sum_digits(1345))
        
#==============largest of 3 numbers======
def largest(nums):
    return max(nums)
print(largest((12,34,56,16)))

#==============gcd of 2 numbers=============
a,b = map(int, input().split())
while b:
    a,b = b, a%b
print(a)
    
#============lcm of 2 numbers=========
a,b = map(int, input().split())
x,y = a,b
while y:
    x,y = y,x%y
gcd = x
lcm=abs(a*b)//gcd
print(lcm)


#============insertion sort============        
def insertionSort():
    pass
