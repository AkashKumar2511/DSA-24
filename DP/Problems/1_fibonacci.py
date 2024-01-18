#                    0 1 2 3 4 5 6
#Fibonacci Numbers : 0 1 1 2 3 5 8 13 .......
#Recursion relation : f(n) = f(n-1) + f(n-2)

"""
1.Recursion
------------
TC : O(2^n)
SC : O(n)
"""
def rec_fibonacci(n):
    if(n <= 1):
        return n
    return rec_fibonacci(n-1) + rec_fibonacci(n-2)

# n = int(input("Enter input number : "))
# print(rec_fibonacci(n))




"""
2.Memoization : Helps in avoiding repetitive computings
--------------
Steps :
    -> Create a dp array of size n+1
    -> Store
    -> Checking if it is previously computed
TC : O(n)
SC : O(n) + O(n) (for recursion stack space and dp array)
"""
def mem_fibonacci(n):
    if(n <= 1):
        return n
    if(dp[n] != -1):
        return dp[n]
    dp[n] = mem_fibonacci(n-1) + mem_fibonacci(n-2)
    return dp[n]
    
# n = int(input("Enter input number : "))
# dp = [-1]*(n+1)
# print(mem_fibonacci(n))


"""
3. Tabulation : The recursion stack space is eliminated
-------------
TC : O(n)
SC : O(n)
"""

n = int(input("Enter input number : "))
dp = [-1]*(n+1)
dp[0], dp[1] = 0, 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])



"""
4. Tabulation + Space Optimization :
-------------
TC : O(n)
SC : O(1)
"""

n = int(input("Enter input number : "))
prev2, prev = 0, 1

for i in range(2, n+1):
    curr = prev + prev2
    prev = curr
    prev2 = prev
print(prev)
