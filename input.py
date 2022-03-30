def text_input() -> str:
    print("Enter 'default' to use default text. Otherwise enter your text.")
    text = input()
    if text == "default":
        with open("text.txt") as f:
            text = f.readlines()
            text = ''.join(text)
    return text


def nk_inpt() -> tuple[int, int]:
    print("\nEnter the n and k for counting top-K n-gramms (default k = 10 and n = 4. Enter newline to leave default "
          "values")
    inp = input()
    if inp == "":
        return 4, 10
    n, k = inp.split()
    return int(n), int(k)