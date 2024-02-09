# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())

phoneBook = {}
for _ in range(size):
    name, phoneNumber = input().split()
    phoneBook[name] = phoneNumber
    

while True:
    try:
        name = input()
        if name not in phoneBook:
            print("Not found")
            continue
            
        print(f'{name}={phoneBook[name]}')
        
    except EOFError:
        break
