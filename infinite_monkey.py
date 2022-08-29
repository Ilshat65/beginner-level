import random
from string import ascii_lowercase


SOURCE_SYMBOLS = ascii_lowercase + ' '
TARGET_SENTENCE = "a computer science portal for geeks"


def create_sentence() -> str:
    result_list = random.choices(SOURCE_SYMBOLS, k=35)
    generated_sentence = ''.join(result_list)
    return generated_sentence


def compare_two_sentences_letterwise() -> int:
    score = 0
    generated_sentence = create_sentence()
    if len(generated_sentence) == len(TARGET_SENTENCE):
        for i in range(0, len(TARGET_SENTENCE)):
            if generated_sentence[i] == TARGET_SENTENCE[i]:
                score += 1
    print(generated_sentence)
    return score


def run():
    try_counter = 0
    best_score_so_far = 0

    while True:
        score = compare_two_sentences_letterwise()

        if score > best_score_so_far:
            best_score_so_far = score

        if score != len(TARGET_SENTENCE):
            try_counter += 1
            print("best score so far:", best_score_so_far)
            print("tries used:", try_counter)
            print("-" * 50)
            continue
            
        else:
            print("Yay ! You got it!")
            break


if __name__  == "__main__":
    run()