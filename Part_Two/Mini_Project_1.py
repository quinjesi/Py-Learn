file = open('Part_Two/students.txt', 'r')
a = file.read()
print(a) 

split1 = a.split('\n')
print(split1)

for i in split1:
    split2 = i.split(' ')
    print(split2)

    sum = int(split2[1]) + int(split2[2]) + int(split2[3])
    print(f"{split2[0]} has a total score of {sum}")

    avg = sum / 3
    print(f"{split2[0]} has an average score of {avg:.2f}")

    if avg >= 15:
        print(f"{split2[0]} has passed the exam")
    else:
        print(f"{split2[0]} has failed the exam")