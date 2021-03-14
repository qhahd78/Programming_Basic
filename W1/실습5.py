# 실습5 의용메카트로닉스공학과 20195277 하유민


from random import randint
print("의용메카트로닉스공학과 20195277 하유민")

secret = randint(1, 10)
print("Welcome!")
guess = 0
again = 0
while guess != secret:
    g= input("Guess the number: ")
    guess = int(g)
    if guess == secret:
        print("You win!")
    else:
        if again == 0 :
            print("틀렸네요")
            again = 1
        else:
            print("또 틀렸네요")
        if guess > secret:
            print("Too high")
        else:
            print("Too low")
print("Game over!")
