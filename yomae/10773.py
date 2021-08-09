# BOJ-10773 제로

N = int(input())
ans = []

for i in range(N):
    a = int(input())
    if a==0:
        ans.pop()
    else:
        ans.append(a)

print(sum(ans)) # sum 함수 :  ans 리스트(정수) 원소들의 총합을 구해줌 