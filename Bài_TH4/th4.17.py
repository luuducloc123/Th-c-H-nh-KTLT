print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
print(" nhap vao so n can tinh tong ca uoc so:  ")
n=int(input())
sum=0
for i in range(1, n+1):
       if (n%i ==0):
          sum+=i
print(" tong tat ca cac uoc so ", n, "la : ", sum)
        
