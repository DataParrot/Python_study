# 프로그래머스
# 에라토스테네스의 체
def solution(n):
    a = [False,False] + [True]*(n-1)  # 인덱스 0과 자연수 1을 False로 제거, # 앞에 2개 추가되니까 n에 -1
    b = []
    
    for i in range(2,n+1):
        if a[i]:  # a의 해당 인덱스가 True일 경우
            b.append(i)  # 해당 숫자를 리스트에 추가
        for j in range(2*i, n+1, i):  # 2를 곱한거부터, n에서 1을 더한거까지 ,i의 간격으로
            a[j] = False  # 해당 숫자는 소수가 아니라서 삭제해야하므로 False라고 지정
    return len(b)  #소수만 담긴 리스트의 길이를 리턴