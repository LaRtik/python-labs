def text_input() -> str:
    print("Enter 'default' to use default text. Otherwise enter your text.")
    text = input()
    if text == "default":
        with open("text.txt") as f:
            text = f.readlines()
            text = ''.join(text)
    return text


def nk_input() -> tuple[int, int]:
    print("\nEnter the n and k for counting top-K n-gramms (default k = 10 and n = 4. Enter newline to leave default "
          "values")
    inp = input()
    if inp == "":
        return 4, 10
    n, k = inp.split()
    return int(n), int(k)


def average_output(average_words: float) -> None:
    print(f"Average words in sentence: {average_words}")


def median_output(median_words: float) -> None:
    print(f"Average words in sentence: {median_words}")


def top_ngramms_output(top_n_gramms: dict, n: int, k: int) -> None:
    print(f"Counted top-{k} {n}-gramms: {top_n_gramms}")


def word_stats_output(words: dict):
    print(words)
