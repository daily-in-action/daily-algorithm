# BOJ-11328 Strfry
def is_valid(str1,str2):
    if len(str1)!=len(str2):
        return False
    
    for i in range(len(first)):
        if first[i]!=second[i]: # 정렬된 리스트 비교중 하나라도 서로 다른 문자가 있다면 재배열 시 동일하게 못만듬
            return False

    return True       
            
N = int(input()) # 테스트 케이스의 수

for i in range(N):
    temp = list(input().split()) # temp[0]과 temp[1]에 각각 문자열이 담긴다
    
    # 문자열을 각각의 문자로 쪼개서 리스트로 + 정렬
    first = list(temp[0]) 
    second = list(temp[1])
    first.sort()
    second.sort()
    
    if is_valid(first,second):
        print("Possible")
    else:
        print("Impossible")
    


