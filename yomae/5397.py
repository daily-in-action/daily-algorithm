# BOJ-5397 키로거
# 처음에 count를 써서 커서를 움직이는 식으로 구현해보려 했으나 매우 복잡한 관계로 (알파벳이 나오지 않은 상태에서 >, <, -만 중복으로 계속 나올 때 처리가 매우 불편했음)
# count 자체를 안쓰고 어떻게 할지 이리저리 고민해보다가 두 개의 배열을 만들어서 스택처럼 만들어 풀어보았다.
import sys

N = int(input())

def process(char, stack_result, stack_temp): # 조건 처리 함수
    if char == '>':
        if len(stack_temp) > 0:
            stack_result.append(stack_temp.pop()) # > 인 경우 temp에서 하나를 뽑아서 result에 넘겨줌
    elif char == '<':
        if len(stack_result) > 0:
            stack_temp.append(stack_result.pop()) # < 인 경우 result에서 하나를 뽑아서 temp로 넘겨줌
    elif char == '-':
        if len(stack_result) > 0:
            stack_result.pop() # - 즉 백스페이스가 나온 경우에 result에서 하나를 지워준다.  
    else:
        stack_result.append(char) # 알파벳 or 숫자이면 result에 넣어줌     

    # else안에 if len(temp)>0 이나 if len(result)>0 조건들은 리스트가 비어있을 때 pop()을 하면 자꾸 에러가 나서 넣어줌.

for i in range(N):
    test = sys.stdin.readline().rstrip()
    temp = []
    result = []

    for j in range(len(test)):
        process(test[j], result, temp)
    
    if len(temp) > 0: # 루프를 다 돌고 나왔을 때 temp에 남아있는 문자가 있을 경우에 역순으로 result에 넘겨줌
        for k in range(len(temp)):
            result.append(temp.pop())

    print(''.join(result))