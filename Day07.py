import re
cur_dir = None  # current directory ptr
 
## Node
class Directory:
    def __init__(self, name, parent, size = 0):
        self.name = name
        self.size = size
        self.children = list()
        self.parent = parent
class File:
    def __init__(self, name, size = 0):
        self.name = name
        self.size = size

# Tree structure
class Tree:
    def __init__(self):
        self.root = Directory(name='/', parent=None)

    # Fn: Insert a child node at a particular node
    def insert(self, child, cur):
        #print(cur.name)
        cur.children.append(child)
        parent = cur
        if child.size > 0:
            while parent:
                parent.size += child.size
                parent = parent.parent

def Day7a(file):
    # Create a filesystem
    filesystem = Tree()
    cur_dir = filesystem.root

    # Read input line by line, and build the filesystem tree
    file1 = open(file, 'r')
    lines = file1.readlines()

    for line in lines:
        result1 = re.search(r"^\$ ls", line)
        result2 = re.search(r"^\$ cd ", line)

        # When encounter ls, ignore that line
        if result1:
            continue
        # When encounter cd, traverse the tree to reach to the destination
        elif result2:
            dir_to_change = line.split()[-1]
            if dir_to_change == "..":
                cur_dir = cur_dir.parent
            elif dir_to_change == "/":
                cur_dir = filesystem.root
            else:
                flag = False
                for child in cur_dir.children:
                    if isinstance(child, Directory) and child.name == dir_to_change:
                        cur_dir = child
                        # print("cd", cur_dir.name)
                        flag = True
                        break
                if not flag:
                    print('Something went wrong')
        # When it is a file/directory, it must be an item from the previous ls command. Add it to the filesystem tree
        else:
            #print(cur_dir.name)
            result3 = re.search(r"^dir ", line)
            if result3: # if dir
                dirname = line.split()[1]
                filesystem.insert(Directory(dirname, cur_dir), cur_dir)
            else: # if file
                size, filename = line.split()
                size = int(size)
                filesystem.insert(File(filename, size), cur_dir)
       
    
    dir_dict = {}
    traverseTree(filesystem.root, dir_dict)

    return sum(dir_dict.values())

def Day7b(file):
    # Create a filesystem
    filesystem = Tree()
    cur_dir = filesystem.root

    # Read input line by line, and build the filesystem tree
    file1 = open(file, 'r')
    lines = file1.readlines()

    for line in lines:
        result1 = re.search(r"^\$ ls", line)
        result2 = re.search(r"^\$ cd ", line)

        # When encounter ls, ignore that line
        if result1:
            continue
        # When encounter cd, traverse the tree to reach to the destination
        elif result2:
            dir_to_change = line.split()[-1]
            if dir_to_change == "..":
                cur_dir = cur_dir.parent
            elif dir_to_change == "/":
                cur_dir = filesystem.root
            else:
                flag = False
                for child in cur_dir.children:
                    if isinstance(child, Directory) and child.name == dir_to_change:
                        cur_dir = child
                        # print("cd", cur_dir.name)
                        flag = True
                        break
                if not flag:
                    print('Something went wrong')
        # When it is a file/directory, it must be an item from the previous ls command. Add it to the filesystem tree
        else:
            #print(cur_dir.name)
            result3 = re.search(r"^dir ", line)
            if result3: # if dir
                dirname = line.split()[1]
                filesystem.insert(Directory(dirname, cur_dir), cur_dir)
            else: # if file
                size, filename = line.split()
                size = int(size)
                filesystem.insert(File(filename, size), cur_dir)
       
    total_disk_space = 70000000
    needed_unused_space = 30000000
    unused_space = total_disk_space - filesystem.root.size
    min_dir_size_to_del = needed_unused_space - unused_space
    #print(min_dir_size_to_del)
    dir_dict = {}
    traverseTree1(filesystem.root, dir_dict, min_dir_size_to_del)

    return min(dir_dict.values())

def traverseTree(root, dir_dict):
    # print(root.size, root.name)
    if isinstance(root, Directory):
        # print(root.children)
        if root.size <= 100000:
            dir_dict[root] = root.size
        for child in root.children:
            # print(child.name)
            # if isinstance(child, Directory):
            #     print("Content for subfolder:")
            #     for c in child.children:
            #         print(c.name)
            traverseTree(child, dir_dict)

def traverseTree1(root, dir_dict, min_size):
    if isinstance(root, Directory):
        if root.size >= min_size:
            dir_dict[root] = root.size
            for child in root.children:
                traverseTree1(child, dir_dict, min_size)

if __name__ == "__main__":
    print("Day7a: ", Day7a("Day7.txt"))
    print("Day7b: ", Day7b("Day7.txt"))