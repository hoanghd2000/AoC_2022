def Day4a(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    count = 0

    for line in lines:
        elf1, elf2 = line.split(',')
        elf1_l, elf1_r = elf1.split('-')
        elf2_l, elf2_r = elf2.split('-')
        elf1_l = int(elf1_l)
        elf1_r = int(elf1_r)
        elf2_l = int(elf2_l)
        elf2_r = int(elf2_r)
        #print(elf1_l, elf1_r, elf2_l, elf2_r)

        if elf1_l <= elf2_l and elf1_r >= elf2_r:
            count += 1
        elif elf1_l >= elf2_l and elf1_r <= elf2_r:
            count += 1
    
    return count

def Day4b(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    count = 0

    for line in lines:
        elf1, elf2 = line.split(',')
        elf1_l, elf1_r = elf1.split('-')
        elf2_l, elf2_r = elf2.split('-')
        elf1_l = int(elf1_l)
        elf1_r = int(elf1_r)
        elf2_l = int(elf2_l)
        elf2_r = int(elf2_r)
        #print(elf1_l, elf1_r, elf2_l, elf2_r)

        if elf1_r >= elf2_l and elf1_l <= elf2_r:
            count += 1
    
    return count

if __name__ == "__main__":
    print("Day4a: ", Day4a("Day4.txt"))
    print("Day4b: ", Day4b("Day4.txt"))