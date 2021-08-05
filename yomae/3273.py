# BOJ-3273 두 수의 합
N = int(input())
sequence = list(map(int,input().split()))
sum = int(input())

head = 0 # 수열의 첫번째 항
tail = N-1 # 수열의 마지막 항
result = 0
sequence.sort() # 오름차순으로 정렬해줌

while(head < tail): # 1씩 증감하므로 head와 tail이 같아지면 루프를 끝낸다.
    sequence_sum = sequence[head]+sequence[tail]
    
    if sequence_sum == sum: # 합이 같다면 쌍의 갯수를 +1한다.
        result += 1

    if sequence_sum > sum: # 양 끝수의 합이 더 크다면 우측 끝 항을 하나 내려준다.
        tail -= 1
    else: # 양 끝수의 합이 더 작다면 좌측 끝 항을 하나 올려준다.
        head += 1  

print(result)