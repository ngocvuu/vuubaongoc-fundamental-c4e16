
def get_even_list(numb_list):
    even_list = []
    for numb in numb_list:
        if numb % 2 == 0:
            even_list.append(numb)
    return even_list


numb_list = [1, 4, 5, -1, 10]
even = get_even_list(numb_list)
# print(even)
