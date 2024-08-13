import random

# Declaring start and end values
start = 0
end = 5

# Welcome text
print(f'Welcome to "A number between {start} and {end}"')
print()

# Game type input
g_type = int(input(f'Type 1 if you would like me to guess your number '

                   '\n' f'or' '\n' f'Type 2 if you would like to guess my number: '))


# Loop to make sure user enters 1 or 2
while g_type not in {1,2}:
        print()
        g_type = int(input(f'Invalid input.{'\n'}Please Type 1 if you would like me to guess your number between {start} and {end} '
                   
            '\n' f'or' '\n' f'Type 2 if you would like to guess my number between {start} and {end}: '))

# Loop to select game based on user input
if g_type == 1:
    print()
    print(f'Great! Now I get to guess your number')
    value = int(input(f'Choose a number between {start} and {end}:  '))
    print()
elif g_type == 2:
    print()
    print(f'Great! Now you get to guess my number')
    value = int(input(f'Guess a number between {start} and {end}:  '))
    print()

# To check if value is within range
if (value > end) or (value < start):
    print(f'Wrong Input')
    value = int(input(f'Guess a number between {start} and {end}:  '))
    print()

# Game 1
while g_type == 1:
    Rnd = random.randint(start, end)

    if value == Rnd:
        print(f"Looks like I guessed your number. It's {value}")
        break
    elif value != Rnd:
        feedback = input(f'is your number higher or lower than {Rnd}?: ').strip().lower()
        print()
        if feedback == 'higher':
            start = Rnd + 1
        elif feedback == 'lower':
            end = Rnd - 1
        elif feedback not in {'higher','lower'}:
            print(f"invalid input. Please indicate higher or lower ")
            print()

# Game 2
Rnd = random.randint(start, end)
while g_type == 2:

    if Rnd == value:
        print(f"Looks like you guessed my number. It's {value}")
        break
    elif Rnd < value:
        print(f'Sorry, {value} is higher than my number. Guess again!')
        value = int(input(f'Guess a number between {start} and {end}:  '))
        print()
    else:
        print(f'Sorry, {value} is lower than my number. Guess again!')
        value = int(input(f'Guess a number between {start} and {end}:  '))
        print()