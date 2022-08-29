import random

USER_MESSAGE = "R --> number is correct and is in the right place\nY --> number is correct and is in the wrong place\nB --> number is incorrect"


def generate_secret_number():
    codes_list = list()
    for _ in range(4):
        val = random.randint(1, 9)
        codes_list.append(str(val))
    return ''.join(codes_list)


def guess():
    user_input = input("Guess a number: ")
    return user_input


def compare_two_numbers():

    possible_numbers = list(range(0, 10, 1))

    secret_number = generate_secret_number()
    lives = 1
    print(USER_MESSAGE)
    print("-" * 25)

    for _ in range(100):
        print("possible_numbers:", possible_numbers)
        if lives > 0:
            user_guess = guess()
            comparison_outcome = ""
            for i in range(4):
                if user_guess[i] == secret_number[i]:
                    comparison_outcome += "R"
                elif user_guess[i] != secret_number[i] and user_guess[i] in secret_number:
                    comparison_outcome += "Y"
                else:
                    if int(user_guess[i]) in possible_numbers:
                        possible_numbers.remove(int(user_guess[i]))
                    comparison_outcome += "B"
        else:
            break

        if comparison_outcome == "RRRR":
            return f"Congrats, you have guessed the secret number: {user_guess}"

        lives -= 1
        print("Result of your guess:", comparison_outcome)
    return f"Sorry, you have used up all of your guesses. Next time lucky.\nThe secret number was {secret_number}"

outcome = compare_two_numbers()
print(outcome)