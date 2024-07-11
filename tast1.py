def most_recurrent_bigrams(keywords):
    from collections import defaultdict

    # Initialize defaultdict to store the number of occurrences of each binary (two-character segment)
    bigram_counts = defaultdict(int)

    # Iterate through each word in the keyword list
    for word in keywords:
        word_length = len(word)

        # Repetition through each diary (two-letter syllable) in a word
        for i in range(word_length - 1):
            # Extract binary from word
            bigram = word[i:i + 2]

            # Increase the number of binary times in the dictionary
            bigram_counts[bigram] += 1

    # Find the first two pairs with the highest number of occurrences in the dictionary
    most_recurrent = sorted(bigram_counts.items(), key=lambda item: item[1], reverse=True)[:2]
    most_recurrent_bigrams = [bigram for bigram, count in most_recurrent]

    return most_recurrent_bigrams


# use example
keywords = ['milk', 'chocolate', 'c+', 'python', 'cat', 'dog']
print(most_recurrent_bigrams(keywords))


