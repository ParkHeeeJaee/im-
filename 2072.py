'''
10개의 수를 입력 받아, 홀수만 더한 값을 출력
각 수는 0 <= x <= 10000
'''

t = int(input())
# tc의 개수 만큼 반복, 
for tc in range(1, t+1):
    numbers = list(map(int, input().split()))
    # 홀수의 갯수를 저장
    sum_odd = 0

    # 입력받을 리스트의 길이만큼 반복
    for i in range(len(numbers)):
        # 2로 나눴을때, 1이 남으면 홀수로 판단
        if numbers[i] % 2 == 1:
            # 위의 경우에 해당하면 1 증가
            sum_odd += numbers[i]

    # 형식에 맞게 출력, f 스트링 tc, sum_odd 값
    print(f'#{tc} {sum_odd}')
