# Uses python3
def calc_fib(n): 
    fibNumbers = [0, 1]
    
    if n < 2:
        return fibNumbers[n]
    
    for i in range(2, n+1): 
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])        
    
    return fibNumbers[n]
         
n = int(input())
print(calc_fib(n))
