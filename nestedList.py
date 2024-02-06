if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
        
    records.sort(key = lambda score : score[0])
    scores.sort()
    min_score = list(set(scores))[1]
    
    for name, score in records:
        if score == min_score:
            print(name)
