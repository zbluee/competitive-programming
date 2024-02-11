n, k = list(map(int, input().split()))

for _ in range(k):
    last_digit = num % 10
    if last_digit == 0:
        n /= 10
    else:
        n -= 1
        
print(int(n))
    
