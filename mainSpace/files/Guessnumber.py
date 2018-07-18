i = 1
low = 0
high = 100
while True:
    mid = int((low + high)/2)
    print("Guess #",i,": Guess Value is ", mid)
    print("If the guess value is equal to your number, press 'y'")
    print("If the guess value is bigger than your number, press 'b'")
    print("If the guess value is smaller to your number, press 's'")
    feedback = input()
    if feedback == 'y':
        print('Congratulations to your computer! Your guess is correct!')
        break
    elif feedback == 'b':
        high = mid -1
    else:
        low = mid + 1
    i = i +1
