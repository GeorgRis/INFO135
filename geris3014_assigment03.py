#1
# 27%13 = 1, 130%13= 0
# answer: B

#2q1
#load factor = number of items/table size = 9/11
#2q2
# answer: D

#3
import hashlib as hl
import random

class HashClass:
    def __init__(self, id_num):
        self.id_num = id_num


    def hash_it(self):
        salt = random.randint(1, 1000)
        self.id_num = hl.sha1(str((self.id_num+salt)).encode()).hexdigest()
        return self.id_num

    def print_it(self):
        hash = HashClass(self.id_num)
        print(hash.hash_it())

my_hash = HashClass(11011999)
my_hash.print_it()

#4
def most_frequent_integer(list):
    dict = {}
    for num in list:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    most_frequent_num = max(dict, key=dict.get)
    return most_frequent_num

my_list = [10, 2, 5, 2, 0, 5, 6, 8, 5, 10]
result = most_frequent_integer(my_list)
print(result)
