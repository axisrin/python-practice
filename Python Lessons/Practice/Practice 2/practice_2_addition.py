s = list()
s.append('1')
s.append('2')
s.append('3')
s.append('1')
s.append('2')
s.append('3')

# Str in Int 2.1
def str_in_int(s):

    # s = list()
    # # s.append('hoq')
    # s.append('1')
    # # s.append('moq')
    # s.append('2')
    # s.append('3')
    print(type(s[0]))
    s = [int(x) for x in s]
    print(type(s[0]))
    return s

str_in_int(s)

# Total natural Nums 2.2
def total_natural_nums_in_list(s):
    temple_s = s
    total_length = len(set(s))
    print(total_length)

total_natural_nums_in_list(s)

print(s)

# Reverse 2.3
def reverse_list(s):
    new_s = s[::-1]
    print(new_s)

reverse_list(s)

# Indexes of elems 2.4
def indexes_list(s):
    x = 2
    index_list = [i for i in range(len(s)) if int(s[i]) == x]
    print(index_list)

indexes_list(s)

# Sum of chet nums 2.5
def total_of_chet_nums(s):
    new_s = str_in_int(s)
    total_of_nums = sum(new_s[::2])
    print(total_of_nums)

total_of_chet_nums(s)