import random
import math

# file = open('my_text_file.txt', 'w')

# li = [0, 1]

# to write the numbers into the file
# for p in range(0, 10):
#     bin = 1
#     dec = 0
#     po = 0
#
#     for i in range(1, 16):
#         bin = bin * 10 + li[random.randint(0, 1)]
#
#     #decimal number
#     for j in str(bin)[::-1]:
#         if j == '1':
#             dec = dec + math.pow(2, po)
#         po = po + 1
#
#     file.write(str(bin))
#     file.write('\t')
#     file.write(str(dec))
#     file.write('\n')

# to read them back, and sort them
file = open('my_text_file.txt', 'r+')

li = file.read().split('\n')
bin_num_list = [int(i[0:16]) for i in li]
dec_num_list = [float(i[17:30]) for i in li]

tup_list = [(a, b) for (a, b) in zip(bin_num_list, dec_num_list)]


def sort_on_second_element(element):
    return element[1]


tup_list.sort(key=sort_on_second_element)

file.write("\n\nAfter Sorting\n")
for i in tup_list:
    file.write(str(i[0]))
    file.write('\t')
    file.write(str(i[1]))
    file.write('\n')
