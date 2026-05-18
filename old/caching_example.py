
def fib(n):
    def recurse_fib(n):
        if n in old_vals:
            return old_vals[n]
        if n==0 or n==1:
            return 1

        old_vals[n]=fib(n-1)+fib(n-2) 
        return fib(n-1)+fib(n-2) 
    old_vals={}
    answer= recurse_fib(n)
    return answer


print(fib(5))