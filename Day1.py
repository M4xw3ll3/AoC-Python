stripper = [int(line.rstrip("\n")) for line in open("AdventofCodingDay1.txt","r")]
print(stripper)

for i in range(0,200):
    for j in range(1,200):
        for k in range(2,200):
            if stripper[i]+stripper[j]+stripper[k]==2020:
                print(stripper[i]*stripper[j]*stripper[k])