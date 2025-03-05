'''
10개의 수를 입력받아, 평균값 출력
! 소수점 첫째 자리에서 반올림한 정수 출력
0 <= x <= 10000
'''

t = int(input())
for tc in range(1, t+1):
    # 입력 받을 값을 map 함수를 사용 공백을 기준으로 int로 입력
    numbers = list(map(int, input().split()))
    # 리스트의 길이
    n = len(numbers)
    
    # 소수점에서 반올림 하기 위해 round 함수 사용
    # int 사용시 반올림이 아니라 소수 부분을 버려버림
    result = round(sum(numbers) / n)

    # 형식에 맞게 출력
    print(f'#{tc} {result}')
