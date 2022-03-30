def average_words(sentence_stats: list) -> float:
    return sum(sentence_stats) / len(sentence_stats)


def median_words(sentence_stats: list) -> float:
    size = len(sentence_stats)
    if size % 2 == 0:
        return (sorted(sentence_stats)[size // 2] + sorted(sentence_stats)[size // 2 - 1]) / 2
    else:
        return sorted(sentence_stats)[size // 2]


def count_ngramms(word_stats: dict, n: int, k: int) -> dict[str, int]:
    result = {}
    for key, value in word_stats.items():
        for i in range(n):
            if i + n > len(key):
                break
            gramma = key[i:i + n]
            if result.get(gramma) is not None:
                result[gramma] += value
            else:
                result[gramma] = value
    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True)[:k])
