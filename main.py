import IO
import parse
import math_stats


def main():
    text = IO.text_input()
    word_stats, sentences_stats = parse.parse_text(text)
    IO.word_stats_output(word_stats)
    IO.average_output(math_stats.average_words(sentences_stats))
    IO.median_output(math_stats.median_words(sentences_stats))
    n, k = IO.nk_input()
    IO.top_ngramms_output(math_stats.count_ngramms(word_stats, n, k), n, k)


if __name__ == '__main__':
    main()
