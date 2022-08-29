def get_best_substring(input_string: str = "") -> str:
    '''
    ```markdown

    input:
        - input_string: [str] (default = "")
    
    output:
        - output_string: [str] (default = None)
    ```
    '''

    possible_options = list()
    start_position = 0
    end_position = len(input_string)


    if len(input_string) != 0:
        while True:
            if start_position != end_position:
                for i in range(start_position + 1, end_position):
                    substring = input_string[start_position:i]
                    if len(substring) == len(set(substring)):
                        if substring not in possible_options:
                            possible_options.append(substring)
                    else:
                        break
                start_position += 1
                continue
            else:
                possible_options.append(input_string[-1])
                print("[INFO] Done")
                break
        
        max_length = len(max(possible_options, key=len))
        print("max_length:", max_length)
        for option in possible_options:
            if len(option) == max_length:
                print("result:", option)
                break
    else:
        print("-1")


get_best_substring("")