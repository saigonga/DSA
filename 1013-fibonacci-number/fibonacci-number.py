class Solution:
    def fib(self, n: int) -> int:
        memo ={0:0,1:1}
        def f(X):
            if X in memo:
                return memo[X]
            else:
                memo[X]= f(X-1)+f(X-2)
                return memo[X]

        return f(n)        
    
