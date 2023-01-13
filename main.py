import random
loop = True


def function():
    randnum1 = 0
    randnum2 = 0
    sum = 0
    randnum1 = random.randrange(1, 7)
    randnum2 = random.randrange(1, 7)
    sum = randnum1 + randnum2
    print(str(randnum1) + "," + str(randnum2) + " (sum: " + str(sum) + ")")


while loop:
    print("\nDice Roll Simulator Menu \n1. Roll Dice Once\n2. Roll Dice 5 Times\n3. Roll Dice 'n' Times \n4. Roll Dice until Snake Eyes\n5. Exit")
    select = int(input("\nSelect an option (1-5):"))
    if select == 1:
        function()
    elif select == 2:
        x = 0
        while x < 5:
            function()
            x += 1
    elif select == 3:
        x = 0
        number = int(input("How many rolls would you like? "))
        while x < number:
            function()
            x += 1
    elif select == 4:
        x = 0
        snake = False
        while snake == False:
            randnum1 = random.randrange(1, 7)
            randnum2 = random.randrange(1, 7)
            sum = randnum1 + randnum2
            print(str(randnum1) + "," + str(randnum2) +
                  " (sum: " + str(sum) + ")")
            x += 1
            if randnum1 == 1 and randnum2 == 1:
                snake = True
                print("SNAKE EYES! It took " + str(x) + " to get snake eyes.")
    else:
        loop = False
