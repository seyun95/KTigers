from operator import index
import random

# 1. 세자릿수 숫자를 만들어 저장하기
# 2. 안내 문구 표시 - "숫자를 입력하세요"
# 3. 입력 받기
# 4. 입력 받은 숫자와 저장된 숫자를 비교하기
# 5. 스트라이크와 볼로 표시하기. 예) 1S / 2B 1S / 1B 2S / 3S
# 6. 3S 이면 게임 끝

def check_answer():   
    correct_numbers = []
    correct_numbers = random.sample(range(1, 10), 3)#세자릿수 만들어 정의하기
    print("숫자를 임력하세요. 같은 숫자 안됨. 예: 123")#안내문구 표시
    anserd = input()#입력 받기

    strike = 0
    boll = 0
    chance = 0
    index_anserd = 0#인데스로 대답을 하나씩 비교할때 쓰는 변수
    while strike < 3:
        if anserd == 'q':
            print('실패하셨습니다.')
            print('정답:',correct_numbers)
            break 
        for correct in correct_numbers:
            correct_str = str(correct) 
            if anserd[index_anserd] == correct_str:
                strike = strike + 1 
                index_anserd = index_anserd + 1
            else:            
                for anserd_boll in anserd:         
                    if correct_str == anserd_boll:
                        boll = boll + 1
                index_anserd = index_anserd + 1 
        print(strike,'s' ,boll,'b') 
        if strike != 3:
            strike = 0
            boll = 0
            chance = chance + 1
            index_anserd = 0 #인데스로 대답을 하나씩 비교할때 쓰는 변수
            print('시도한 횟수:',chance,'(그만하고 싶으시면 q라고 쓰세요)')
            print("숫자를 임력하세요 예: 123")#안내문구 표시
            anserd = input()#입력 받기

    if strike == 3:       
        print('시도한 횟수:',chance)
        print('축하합니다!!') 


check_answer()
