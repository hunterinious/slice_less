def slice_less1(my_list, lesser):
    my_list = [l for l in my_list if l > lesser]
    return sorted(my_list, reverse=True)


def slice_less2(my_list, lesser):
    sorted_list = sorted(my_list, reverse=True)
    for i, l in enumerate(sorted_list):
        if l < lesser:
            return sorted_list[:i - 1]


my_list = [8, 9, 7, 0 , -2 , 3, -1, -2, 5, 12, 14, 0, 4, -4, -2, 5, 1]

print("First option:")
print(slice_less1(my_list, 4))
print("\nSecond option:")
print(slice_less2(my_list, 4))
