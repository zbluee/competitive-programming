n = int(input())
    arr = map(int, input().split())
    scores = list(set(arr))
    max_= max(scores)
    up_score = -101
    
    for score in scores:
        if score > up_score and score < max_:
            up_score = score
            
    print(up_score)
