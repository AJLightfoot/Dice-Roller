import random

prompt = "\nWelcome to my Dice Roller."
prompt += "\n(Type the dice to roll (d4, d6, d8, d10, d12, d20)"
prompt += "\n(Enter q to quit.): "

active = True

while active:
    message = input(prompt)

    if message == 'q':
        active = False
        print("\nThanks for rolling with me.")

    elif message == 'd4':
        d4 = random.randint(1, 4)
        print("\nYour D4 rolled a: " + str(d4))

    elif message == 'd6':
        d6 = random.randint(1, 6)
        print("\nYour D6 rolled a: " + str(d6))

    elif message == 'd8':
        d8 = random.randint(1, 8)
        print("\nYour D8 rolled a: " + str(d8))

    elif dice == 'd10':
        d10 = random.randint(1, 10)
        print("\nYour D4 rolled a: " + str(d10))

    elif dice == 'd12':
        d12 = random.randint(1, 12)
        print("\nYour D4 rolled a: " + str(d12))

    else:
        d20 = random.randint(1, 20)
        print("\nYou rolled a: " + str(d20))