data = [x.replace('\n', '') for x in open("Day6.txt", 'r').read().split('\n\n')]
counter = 0
for word in data:
    nWord = ''
    for letter in word:
        if letter not in nWord:
            nWord = nWord + letter
    counter += len(nWord)
print(counter)
