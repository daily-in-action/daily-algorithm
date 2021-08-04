# BOJ-2577 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

zero_to_nine = [0]*10 # 0~9 갯수 저장할 배열

temp = str(A*B*C) # 곱한 결과값을 문자열로

for i in range(len(temp)): # ex) 첫 자릿수가 4이면 -> zero_to_nine[4]를 +1 해줌. 
    zero_to_nine[int(temp[i])]+=1

for j in range(len(zero_to_nine)): # 결과물 출력
    print(zero_to_nine[j])