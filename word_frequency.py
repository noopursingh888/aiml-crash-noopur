def count_words(sentence):

    words = sentence.lower().split()

    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1

        else:
            frequency[word] = 1

    return dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))


sentence = "Python is easy and Python is powerful"

result = count_words(sentence)

print(result)


# collections.Counter automatically counts word frequency
# It can replace the whole counting function in one line