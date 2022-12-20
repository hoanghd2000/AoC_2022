def Day1a(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    inventory = []
    total = 0

    for line in lines:
        if line == "\n":
            inventory.append(total)
            total = 0
        else:
            total += int(line)

    return max(inventory)

def Day1b(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    inventory = []
    total = 0

    for line in lines:
        if line == "\n":
            inventory.append(total)
            total = 0
        else:
            total += int(line)

    inventory.sort(reverse=True)
    return sum(inventory[:3])

if __name__ == "__main__":
    print("Day1a: ", Day1a("Day1.txt"))
    print("Day1b: ", Day1b("Day1.txt"))