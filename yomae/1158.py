# BOJ-1158 요세푸스 문제

N, K = map(int, input().split())

cnt = 0 # 지워질 사람 자리
ans = [] # 결과 저장

circle = []
for i in range(N): # 1~N까지 리스트 생성
    circle.append(i+1) 

for j in range(N):
    cnt += K-1
    if cnt >= len(circle): # K-1만큼 더했을 때 인덱스 범위가 넘어가면
        cnt %= len(circle) # cnt를 남은 인원수로 나눈 나머지 값 => 자리 번호
    
    ans.append(str(circle.pop(cnt))) # 자리를 pop하여 빼준 후에 ans에 넣어준다. / str로 변환한 이유 -> 뒤에 join문 사용할때 int로 들어가면 에러가 뜸

print('<'+', '.join(ans)+'>')