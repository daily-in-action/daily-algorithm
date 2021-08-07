# BOJ-10773 제로

N = int(input())
ans = []
result = 0

for i in range(N):
    a = int(input())
    if a==0:
        if len(ans)==0:
            ans.append(a)
        else:
            ans.pop()
    else:
        ans.append(a)

for j in range(len(ans)):
    result += ans[j]

print(result)