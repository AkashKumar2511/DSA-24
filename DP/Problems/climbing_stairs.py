# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

"""
1.Recursion
------------
TC : O(2^n)
SC : O(n)
"""
def rec_cs(n):
    if(n <= 2) : return n
    
    return rec_cs(n-1) + rec_cs(n-2)

n = int(input("Enter number : "))
print(rec_cs(n))




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
def mem_cs(n):
    if(n <= 2):
        return n
    if(dp[n] != -1):
        return dp[n]

    dp[n] = rec_cs(n-1) + rec_cs(n-2)
    return dp[n]

dp = [-1]*(n+1)
n = int(input("Enter number : "))
print(mem_cs(n))





"""
3. Tabulation : The recursion stack space is eliminated
-------------
TC : O(n)
SC : O(n)
"""
n = int(input("Enter number : "))
dp = [-1] * (n+1)
dp[1], dp[2] = 1, 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[n])




"""
4. Tabulation + Space Optimization :
-------------
TC : O(n)
SC : O(1)
"""
n = int(input("Enter number : "))
prev2, prev = 1, 2
for i in range(3, n+1):
    curr = prev2 + prev
    prev2 = prev
    prev = curr
print(prev)