print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
def print_pascal_triangle(height):
    for i in range(height):
        print(' ' * (height - i), end='')
        number = 1
        for j in range(i + 1):
            print(number, end=' ')
            number = number * (i - j) // (j + 1)
        print()
n = int(input("Nhập số dòng của tam giác Pascal: "))
print_pascal_triangle(n)

