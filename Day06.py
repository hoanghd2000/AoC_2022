def Day6a(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()
    line = lines[0]

    char_dict = {}
    no_of_unique = 0
    l = 0
    for i in range(4):
        temp = char_dict.get(line[i], 0)
        if temp == 0:
            no_of_unique += 1
        char_dict[line[i]] = temp + 1
    
    # Edge Case
    if no_of_unique == 4:
        return 4
    
    for r in range(4, len(line)):
        # Add the new char
        temp = char_dict.get(line[r], 0)
        if temp == 0:
            no_of_unique += 1
        char_dict[line[r]] = temp + 1

        # Remove the char out-of-range
        temp = char_dict.get(line[l], 0)
        if temp == 1:
            no_of_unique -= 1
        char_dict[line[l]] = temp - 1
                
        l += 1
        if no_of_unique == 4:
            return r+1

def Day6b(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()
    line = lines[0]

    char_dict = {}
    no_of_unique = 0
    l = 0
    for i in range(14):
        temp = char_dict.get(line[i], 0)
        if temp == 0:
            no_of_unique += 1
        char_dict[line[i]] = temp + 1
    
    # Edge Case
    if no_of_unique == 14:
        return 14
    
    for r in range(14, len(line)):
        # Add the new char
        temp = char_dict.get(line[r], 0)
        if temp == 0:
            no_of_unique += 1
        char_dict[line[r]] = temp + 1

        # Remove the char out-of-range
        temp = char_dict.get(line[l], 0)
        if temp == 1:
            no_of_unique -= 1
        char_dict[line[l]] = temp - 1
                
        l += 1
        if no_of_unique == 14:
            return r+1

if __name__ == "__main__":
    print("Day6a: ", Day6a("Day6.txt"))
    print("Day6b: ", Day6b("Day6.txt"))