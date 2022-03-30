import input
import parse
import math_stats


def main():
    text = input.text_input()
    word_stats, sentences_stats = parse.parse_text(text)
    print(word_stats)
    print(f"Average words in sentence: {math_stats.average_words(sentences_stats)}")
    print(f"Median words in sentence: {math_stats.median_words(sentences_stats)}")
    n, k = input.nk_inpt()
    print(f"Counted top-{k} {n}-gramms: {math_stats.count_ngramms(word_stats, n, k)}")


if __name__ == '__main__':
    main()
