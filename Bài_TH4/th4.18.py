print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
def fibonacci_less_than_n(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list
# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))
fibonacci_numbers = fibonacci_less_than_n(n)
# In danh sách số Fibonacci
print("Các số Fibonacci nhỏ hơn", n, "là:", fibonacci_numbers)
