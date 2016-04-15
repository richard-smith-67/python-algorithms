# Uses python3
import sys

def get_fibonacci_last_digit(n):
    # write your code here
    fibNumbers = [0, 1]
    
    if n < 2:
        return fibNumbers[n]
    
    for i in range(2, n+1): 
        fibNumbers.append((fibNumbers[i-1] + fibNumbers[i-2]) % 10)         
    
    return fibNumbers[n]
    
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
