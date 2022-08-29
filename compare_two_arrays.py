import random
import array as arr


def generate_two_arrays():
    array_1 = sorted(
        arr.array(
            'i', 
            [random.randint(1, 10) for _ in range(5)]
        )
    )
    array_2 = sorted(
        arr.array(
            'i', 
            [random.randint(1, 10)**2 for _ in range(5)]
        )
    )

    print("array_1: ", array_1)
    print("array_2: ", array_2)
    return (array_1, array_2)

def compare_two_arrays():
    two_arrays = generate_two_arrays()
    array_1 = two_arrays[0]
    array_2 = two_arrays[1]

    score = 0
    for i in range(0, len(array_1)):
        if array_1[i]**2 == array_2[i]:
            score += 1
    if score == len(array_1):
        return True
    else:
        return False

two_arrays_are_equal = compare_two_arrays()
print(two_arrays_are_equal)