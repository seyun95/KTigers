import random

# 1. 세자릿수 숫자를 만들어 저장하기
# 2. 안내 문구 표시 - "숫자를 입력하세요"
# 3. 입력 받기
# 4. 입력 받은 숫자와 저장된 숫자를 비교하기
# 5. 스트라이크와 볼로 표시하기. 예) 1S / 2B 1S / 1B 2S / 3S
# 6. 3S 이면 게임 끝

correct_numbers = []
correct_numbers = random.sample(range(1, 10), 3)#세자릿수 만들어 정의하기
print("숫자를 임력하세요 예: 1 2 3")#안내문구 표시
index = 0 #인데스로 대답을 하나씩 비교할때 쓰는 변수
strike = 0
anserd = str(input())#입력 받기
while strike == 3:#요기가 돌지 않음
    for correct in correct_numbers:
        if correct == anserd[index]:
            print("1S")
            strike + 1
        else:
            print('1B')    
        index + 1
    if strike != 3:
        print("숫자를 임력하세요 예: 1 2 3")#안내문구 표시
        index = 0 #인데스로 대답을 하나씩 비교할때 쓰는 변수
        anserd = input().split()#입력 받기
