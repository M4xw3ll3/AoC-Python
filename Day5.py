import itertools
with open('AdventofCodingDay5.txt', 'r') as file:
    data = file.read().split('\n')
ID = 0
IDs = []
res1 = 0
res2 = 0
for passe in data:
    binary1 = []
    binary2 = []
    for x in passe[:-3]:
        if x =='F':
            binary1.append(0)
        else:
            binary1.append(1)
    for y in passe[-3:]:
        if y =='L':
            binary2.append(0)
        else:
            binary2.append(1)
    res1 = int("".join(str(x) for x in binary1), 2)
    res2 = int("".join(str(x) for x in binary2), 2)
    IDs.append(res1*8+res2)
    print(IDs)
for i in itertools.combinations(IDs,2):
        if abs(i[0]-i[1]) == 2:
                if not (min(i)+1) in IDs:
                    print(min(i)+1)
