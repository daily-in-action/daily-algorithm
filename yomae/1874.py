# BOJ-1874 스택 수열
# 굳이 stack에서 pop 한 것을 저장할 필요없이 연산 결과만 저장하자. 이거때문에 쓸데없이 시간 날림

N = int(input())

arr = []
for _ in range(N): # 만들어야할 수열 입력받기
    arr.append(int(input()))

stack = [] # push한 것을 잠시 저장하는 공간
push_pop = [] # push와 pop 연산 과정을 저장

def cal_push_pop(arr, stack, push_pop):
    cnt = 1
    for i in range(N):
        while cnt <= arr[i]: # 입력된 수열의 i번째 값까지 push
            stack.append(cnt)
            push_pop.append("+")
            cnt += 1
        
        if stack[-1] == arr[i]: # 스택의 TOP 값과 입력된 수열의 i번째 값이 일치한다면
            stack.pop() # stack에서 pop해줌
            push_pop.append("-")

        else: # 만약에 스택의 TOP값이 입력된 수열의 i번째 값보다 작거나 크다면 입력된 수열과 같은 수를 만들어 낼 수가 없다.
              # TOP값이 큰 경우 : 입력한 수를 꺼내기 위해서 계속 pop을 해야됨 -> 그 수까지 가는동안 pop한 것들이 버려지므로 불가능
              # TOP값이 작은 경우 : ?? 이런 경우는 없는 것 같음 / 스택에 오름차순으로 들어가기 때문에
            return False # 못 만들게 될 시 False 리턴   
    return True # 정상적으로 만들어졌다면 True 리턴

if cal_push_pop(arr, stack, push_pop): # True
    for j in push_pop:
        print(j)
else: # False
    print("NO")




     
    
        


