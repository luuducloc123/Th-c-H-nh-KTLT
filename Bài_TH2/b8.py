print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
a,b = 1, 2
total =0
print (a, end= " ")
while (a <= 4000-1):
    if a%2==0:
        total += a
    a, b = b, a+b
    print( a, end= " ")
print ("/n sum of prime numbers tern in fibonacci series: ", total)
