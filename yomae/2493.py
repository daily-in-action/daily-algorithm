# BOJ-2493 탑

N = int(input())
tower_height = list(map(int,input().split()))
stack_tower = []
ans = []

for i in range(N):
    while stack_tower: # 스택이 차 있는 경우
        if stack_tower[-1][1] < tower_height[i]: # 스택 TOP의 높이가 입력받은 타워 높이보다 낮은 경우
            stack_tower.pop() # 필요 없어진 타워 -> pop
        else: # 스택 TOP의 높이가 입력받은 타워 높이보다 높은 경우
            break # 신호를 수신하는 탑 = 스택 TOP
    
    if stack_tower: # 스택이 차 있는 경우
        ans.append(str(stack_tower[-1][0] + 1)) # 스택 TOP의 INDEX+1 을 저장
    else:
        ans.append("0") # 스택이 비어 있는 경우 = 좌측에 입력받은 타워 높이보다 높은 타워가 없음 = 신호 수신하는 탑 존재 X -> 0
    
    stack_tower.append((i, tower_height[i])) # 입력받은 타워의 INDEX와 높이 push

print(' '.join(ans))
        
        



    
