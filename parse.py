import re

def parse_text(text: str) -> tuple[dict[str, int], list[int]]:
    sentences = re.split(r'[.!?]\s', text)
    sentences_stats = []
    words_stats = {}
    # re.findall(r'\w+[\.,\,\-]\w+|\w+', sentences) <- to find words within sentences
    for sentence in sentences:
        sentence_splited = sentence.strip("\n").rsplit(" ")
        sentences_stats.append(len(sentence_splited))
        for word in sentence_splited:
            if words_stats.get(word) is not None:
                words_stats[word] += 1
            else:
                words_stats[word] = 1
    return words_stats, sentences_stats