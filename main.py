import input
import parse
import math_stats


def main():
    text = input.text_input()
    word_stats, sentences_stats = parse.parse_text(text)
    input.word_stats_output(word_stats)
    input.average_output(math_stats.average_words(sentences_stats))
    input.median_output(math_stats.median_words(sentences_stats))
    n, k = input.nk_input()
    input.top_ngramms_output(math_stats.count_ngramms(word_stats, n, k), n, k)


if __name__ == '__main__':
    main()
