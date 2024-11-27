print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
A=[2,47,8,100,52,141]
max = A[0]
for i in range (len(A)):
    if A[i] > max:
        max = A[i]
    i=i+1
for k in range (len(A)):
    if A[k] == max:
        print ("Giá trị lớn nhất là:", max, "Vị trí thứ:", k)
min = A[0]
for i in range (len(A)):
    if A[i] < min:
        min = A[i]
    i=i+1
for k in range (len(A)):
    if A[k] ==min:
        print ("Giá trị nhỏ nhất là:", min, "Vị trí thứ:", k)
