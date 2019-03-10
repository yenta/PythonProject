#coding=utf-8
import random
game_count = 0
all_count = list()
while True:
    game_count+=1
    guess_count=0
    answer=random.randint(0,99)
    while True:
        guess = int(input("請輸入一個數字(0-99)"))
        guess_count += 1
        interval=abs(guess-answer)
        if interval < 3 and interval >0:
            print("快接近了,但..")
        if guess > answer:
            print("你輸入的數字太大")
        elif guess < answer:
            print("你輸入的數字太小")
        else:
            print("猜對了!")
            print("你總共猜了"+ str(guess_count) + "次")
            all_count.append(guess_count)
            break
    onemore=input("你還要再玩一次嗎?Y/N")
    if onemore.upper() != 'Y':
        print("下次再來玩")
        print("你的成績如下:")
        print(all_count)
        print("平均猜中次數:" + str(sum(all_count)/float(len(all_count))))
        break

    

