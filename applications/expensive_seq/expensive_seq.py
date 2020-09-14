# Your code here

#from hashtable import HashTable


def expensive_seq(x, y, z, ht={}):
    if (x, y, z) in ht:
        return ht[(x, y, z)]

    if x <= 0:
        ht[(x, y, z)] = y + z
    elif x > 0:
        ht[(x, y, z)] = expensive_seq(x - 1, y + 1, z, ht) + expensive_seq(x - 2, y + 2, z * 2, ht) + expensive_seq(x - 3, y + 3, z * 3, ht)

    return ht[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
