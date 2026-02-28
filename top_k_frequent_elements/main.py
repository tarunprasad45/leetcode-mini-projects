from collections import Counter

def top_k_frequent_words(text, k):
    words = text.lower().split()
    frequency = Counter(words)
    return frequency.most_common(k)


if __name__ == "__main__":
    sample_text = """
    data data python python python sql sql leetcode kaggle kaggle kaggle kaggle
    """

    k = 3
    result = top_k_frequent_words(sample_text, k)

    print(f"Top {k} most frequent words:")
    for word, count in result:
        print(f"{word}: {count}")
        




