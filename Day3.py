
with open("AdventofCodingDay3.txt") as f:
    lanes = [line.rstrip("\n") for line in f.readlines()]
count1 = 0
count2 = 0
count3 = 0
count4 = 0
countv = 0
skip = 0

amount1 = 0
amount2 = 0
amount3 = 0
amount4 = 0
amountv = 0

for x in lanes:
    if x[count1] == "#":
        amount1+=1
    count1 = (count1 + 1)%31
    if x[count2] == "#":
        amount2+=1
    count2 = (count2 + 3)%31
    if x[count3] == "#":
        amount3+=1
    count3 = (count3 + 5)%31
    if x[count4] == "#":
        amount4+=1
    count4 = (count4 + 7)%31
    if skip==0:
        countv = (countv + 1)%31
        if x[countv] == "#":
            amountv+=1
    skip = (skip+1)%2
print(amount1)
print(amount2)
print(amount3)
print(amount4)
print(amountv)
print(amount1*amount2*amount3*amount4*amountv)
