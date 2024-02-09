size = int(input())
initial, entered = map(int, input().split())
curr_cap = initial + entered
sufficient = curr_cap
for _ in range(size - 1):
    leave, enter = map(int, input().split())
    curr_cap += enter - leave
    sufficient = max(sufficient, curr_cap)
    
print(sufficient)
