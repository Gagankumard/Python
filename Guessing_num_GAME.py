secret_num=8
guess_limit=3
guess_count=0
while guess_count < guess_limit:
    guess=int(input("Guess a Number Between 1 - 10 : "))
    guess_count+=1
    if guess == secret_num:
        print("You Won!")
        break
    # else:
    #     print("You Lost")
        
else:
    print("You Guess wrong answer 3 times and Exceded the Limit")