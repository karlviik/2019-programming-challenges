from sys import stdin

for sentence in stdin:
    if sentence == '':
        break
    words = sentence.split()
    nwords = []
    for word in words:
        nwords.append(word[::-1])

    sentence = " ".join(nwords)
    print(sentence)
