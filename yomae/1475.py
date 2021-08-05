# BOJ-1475 방 번호
N = input()

basic = [0]*10 # 0~9 숫자 개수를 담을 배열
basic_max = 0 # 6,9의 개수를 제외한 숫자의 갯수중 가장 큰 것을 세트의 갯수로 생각할 수 있다.
sum = 0 # 6,9가 나온 총 갯수 -> 6,9를 같은 수로 치기 때문

for i in range(len(N)):
    if int(N[i])==6 or int(N[i])==9: # 6과 9는 따로 담는다.
        sum+=1
    else:
        basic[int(N[i])]+=1

basic_max = max(basic) 

if sum%2==0: # 한세트로 6,9를 만들 수 있기 때문에 2로 나눈 연산을 해주면 총 세트의 갯수를 알 수 있다.
    sum = sum//2
else:
    sum = sum//2+1

print(max(basic_max,sum)) # 6,9 외에 제일 많이 나온 수(세트수)와 비교해준다.

   





        
        



