import random
num=random.randint(1,100)
numm=0
print("1부터 100 사이의 숫자를 맞추시오")

while True:
    guess=int(input("숫자를 입력하시오: "))
    numm+=1
    if guess>num:
        print("높음!")
    elif guess<num:
        print("낮음!")
    else:
        print("축하합니다. 시도횟수=%d" %numm)
        break
