import sys

big_range = range(1000)

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []
for val in big_range:
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
