with open('AdventofCodingDay4.txt', 'r') as file:
    data = file.read().split('\n\n')
    data = [p.split() for p in data]

p_values = [0, 0, 0, 0, 0, 0, 0]
values = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_colour = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
answer = 0
dic_tmp = {}
list_dic = []
with open("AdventofCodingDay4.txt") as f:
    lanes = [line.rstrip("\n") for line in f.readlines()]
lanes = [line.split(" ") for line in lanes]
for line in lanes:
    for x in line:
        if x == '':
            list_dic.append(dic_tmp)
            dic_tmp = {}
        else:
            dic_tmp[x.split(":")[0]] = x.split(":")[1]

for passports in list_dic:
    for key, value in passports.items():
        if key == "byr":
            if 1920 <= int(value) <= 2002:
                p_values[values.index(key)] += 1
        if key == "iyr":
            if 2010 <= int(value) <= 2020:
                p_values[values.index(key)] += 1
        if key == "eyr":
            if 2020 <= int(value) <= 2030:
                p_values[values.index(key)] += 1
        if key == 'hgt':
            if value[-2:] == 'in':
                if 59 <= int(value[:-2]) <= 76:
                    p_values[values.index(key)] += 1

            if value[-2:] == 'cm':
                if 150 <= int(value[:-2]) <= 193:
                    p_values[values.index(key)] += 1
        if key == 'hcl':
            if value[0] == '#' and value[1:].isalnum() and len(value[1:]) == 6:
                p_values[values.index(key)] += 1
        if key == 'ecl':
            if value in eye_colour:
                p_values[values.index(key)] += 1
        if key == 'pid':
            if len(value) == 9 and value.isdigit():
                p_values[values.index(key)] += 1
    if 0 not in p_values:
        answer += 1
    p_values = [0, 0, 0, 0, 0, 0, 0]
print(answer)
