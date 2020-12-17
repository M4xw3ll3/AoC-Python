import collections as c

data = [x for x in open("Day6.txt", 'r').read().split('\n\n')]
ndata = {}
for x in data:
    ndata[x.replace('\n', '')] = x.count('\n') + 1
data = ndata
roral = 0
for key in data:
    rount = 0
    list_of_letters = c.defaultdict(int)
    for x in key:
        list_of_letters[x] += 1
    print(list_of_letters)
    for i in list_of_letters:
        if list_of_letters[i] == data[key]:
            rount += 1
    roral += rount

print(roral)
