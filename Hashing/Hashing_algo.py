arr = [22, 23, 47, 82, 92, 522, 42, 62, 12, 2]

def simple_hashing(arr):
    hash_table = [0] * 10
    for i in arr:
        index = i % 10
        print(f'Hash_table[{index}] = {i}')
        if hash_table[index] != 0:
            print("colision")
            break
        hash_table[index] = i

simple_hashing(arr)

# chainging hashing (Linked List)
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def chaining_hashing(arr):
    hash_table = [None] * 10
    for i in arr:
        index = i % 10
        print(f'Hash_table[{index}] = {i}')
        data = Node(i, hash_table[index])
        hash_table[index] = data
    return hash_table

def print_hash_table(hash_table):
    for index, node in enumerate(hash_table):
        print(f"Index {index}: ", end="")
        values = []
        while node is not None:
            values.append(node.value)
            node = node.next
        print(" -> ".join(map(str, values)) if values else "None")

hash_table = chaining_hashing(arr)
print_hash_table(hash_table)

# linear Probing
def Linear_Prob_hash(arr):
    hash_table = [0] * 10
    for k in arr:
        isEmpty = False
        i = 0
        while(not isEmpty):
            index = (k + i) % 10
            if(hash_table[index] == 0):
                isEmpty = True
                print(f'Linear_Prob_hash[{index}] = {k}')
                hash_table[index] = k
            else:
                print(f"{index} ->", end = " ")
                i += 1

Linear_Prob_hash(arr)

# quadritic Probing
def quad_probe_hash(arr):
    hash_table = [0] * 100
    for k in arr:
        isEmpty = False
        i = 0
        while(not isEmpty):
            index = (k + (i ** 2)) % 100
            if(hash_table[index] == 0):
                isEmpty = True
                print(f'quad_probe_hash[{index}] = {k}')
                hash_table[index] = k
            else:
                print(f"{index} ->", end = " ")
                i += 1

quad_probe_hash(arr)

# double hashing
def Double_hash(arr):
    hash_table = [0] * 100
    for k in arr:
        def Hash1(k):
            return k % 5
        def Hash2(k):
            return (k ** 2) % 10
        isEmpty = False
        i = 0
        while(not isEmpty):
            hash1_result = Hash1(k)
            hash2_result = Hash2(k)
            index = (hash1_result + (i * hash2_result)) % 100
            print(f"k = {k} | {index} = ({hash1_result} + ({i} * {hash2_result})) % 100")
            if hash_table[index] == 0:
                isEmpty = True
                print(f'Double_hash[{index}] = {k}')
                hash_table[index] = k
            else:
                print(f"{index} ->", end = " ")
                i += 1

Double_hash(arr)