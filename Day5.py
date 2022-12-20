def Day5a(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    for line in lines:
        # Processing the tokens
        tokens = line.split()
        nums = []
        for token in tokens:
            if token.isnumeric():
                nums.append(int(token))
        
        for i in range(nums[0]):
            if stacks[nums[1]-1]:
                temp = stacks[nums[1]-1].pop()
                stacks[nums[2]-1].append(temp)
    
    res = ""
    for i in range(len(stacks)):
        res += stacks[i][-1]
    return res

def Day5b(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    for line in lines:
        # Processing the tokens
        tokens = line.split()
        nums = []
        for token in tokens:
            if token.isnumeric():
                nums.append(int(token))
        
        temp_stack = []
        for i in range(nums[0]):
            if stacks[nums[1]-1]:
                temp = stacks[nums[1]-1].pop()
                temp_stack.append(temp)
        for i in range(nums[0]):
            if temp_stack:
                temp = temp_stack.pop()
                stacks[nums[2]-1].append(temp)
    
    res = ""
    for i in range(len(stacks)):
        res += stacks[i][-1]
    return res

if __name__ == "__main__":
    stacks = [['R', 'G', 'H', 'Q', 'S', 'B', 'T', 'N'],
          ['H', 'S', 'F', 'D', 'P', 'Z', 'J'],
          ['Z', 'H', 'V'],
          ['M', 'Z', 'J', 'F', 'G', 'H'],
          ['T','Z','C','D','L','M','S','R'],
          ['M', 'T', 'W', 'V', 'H', 'Z', 'J'],
          ['T', 'F', 'P', 'L', 'Z'],
          ['Q', 'V', 'W', 'S'],
          ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']]
    
    #print("Day5a: ", Day5a("Day5.txt"))
    print("Day5b: ", Day5b("Day5.txt"))