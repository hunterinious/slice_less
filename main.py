def slice_less1(li, lesser):
    li = [l for l in li if l > lesser]
    return sorted(li, reverse=True)


def slice_less2(li, lesser):
    sorted_li = sorted(li, reverse=True)
    for i, l in enumerate(sorted_li):
        if l < lesser:
            return sorted_li[:i - 1]


li = [8, 9, 7, 0 , -2 , 3, -1, -2, 5, 12, 14, 0, 4, -4, -2, 5, 1]

print("First option:")
print(slice_less1(li, 4))
print("\nSecond option:")
print(slice_less2(li, 4))
