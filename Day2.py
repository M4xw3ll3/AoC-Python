min_max_val = [line.split(" ")[0].split("-") for line in open("AdventofCodingDay2.txt","r")]
letter_val = [line.split(" ")[1].split(":")[0] for line in open("AdventofCodingDay2.txt","r")]
pass_val = [line.split(" ")[2].split("\n")[0] for line in open("AdventofCodingDay2.txt","r")]
place = 0
correct_pass= 0
for x in pass_val:
    if x[int(min_max_val[place][0])-1] == letter_val[place] and x[int(min_max_val[place][1])-1] == letter_val[place]:
        place += 1
        continue
    if x[int(min_max_val[place][0])-1] != letter_val[place] and x[int(min_max_val[place][1])-1] != letter_val[place]:
        place += 1
        continue
    else:
        correct_pass += 1
    place += 1
print(correct_pass)
