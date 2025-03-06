'''

'''

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    lst = [2,3,5,7,11]
    nums = []

    # 리스트 안의 내용에 대해 반복
    for i in lst:
        cnt = 0
        # n의 나머지가 1 이 될 때까지.
        while n % i == 0:
            # 몪을 n에 저장
            n //= i
            # cnt + 1
            cnt += 1
        # 리스트에 추가
        nums.append(cnt)
    
    print (f'#{tc}', *nums)
    
    