def Day3a(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    prio_sum = 0

    for line in lines:
        item_set = set()
        mid = (len(line)-1) // 2
        for i in range(mid):
            item_set.add(line[i])
        
        for i in range(mid, len(line)-1):
            if line[i] in item_set:
                if line[i].islower():
                    prio_sum += (ord(line[i]) + 1 - ord('a'))
                else:
                    prio_sum += (ord(line[i]) + 27 - ord('A'))
                break
    
    return prio_sum

def Day3b(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    prio_sum = 0

    for l in range(0, len(lines), 3):
        item_set_1 = set()
        item_set_2 = set()
        item_set_3 = set()
        
        for i in range(len(lines[l])-1):
            item_set_1.add(lines[l][i])
        
        for i in range(len(lines[l+1])-1):
            item_set_2.add(lines[l+1][i])
        
        for i in range(len(lines[l+2])-1):
            item_set_3.add(lines[l+2][i])

        # print(item_set_1)
        # print(item_set_2)
        # print(item_set_3)
        res_set = item_set_1.intersection(item_set_2, item_set_3)
        badge = res_set.pop()
        # print(badge)
        
        if badge.islower():
            prio_sum += (ord(badge) + 1 - ord('a'))
        elif badge.isupper():
            prio_sum += (ord(badge) + 27 - ord('A'))
    
    return prio_sum

if __name__ == "__main__":
    print("Day3a: ", Day3a("Day3.txt"))
    print("Day3b: ", Day3b("Day3.txt"))