def Day2a(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    total = 0

    for line in lines:
        plays = line.split()
        if plays[0] == 'A':
            if plays[1] == 'X':
                total += 4
            elif plays[1] == 'Y':
                total += 8
            elif plays[1] == 'Z':
                total += 3
        elif plays[0] == 'B':
            if plays[1] == 'X':
                total += 1
            elif plays[1] == 'Y':
                total += 5
            elif plays[1] == 'Z':
                total += 9
        elif plays[0] == 'C':
            if plays[1] == 'X':
                total += 7
            elif plays[1] == 'Y':
                total += 2
            elif plays[1] == 'Z':
                total += 6

    return total

def Day2b(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    total = 0

    for line in lines:
        plays = line.split()
        if plays[0] == 'A':
            if plays[1] == 'X':
                total += 3
            elif plays[1] == 'Y':
                total += 4
            elif plays[1] == 'Z':
                total += 8
        elif plays[0] == 'B':
            if plays[1] == 'X':
                total += 1
            elif plays[1] == 'Y':
                total += 5
            elif plays[1] == 'Z':
                total += 9
        elif plays[0] == 'C':
            if plays[1] == 'X':
                total += 2
            elif plays[1] == 'Y':
                total += 6
            elif plays[1] == 'Z':
                total += 7

    return total

if __name__ == "__main__":
    print("Day2a: ", Day2a("Day2.txt"))
    print("Day2b: ", Day2b("Day2.txt"))