print ( " sv: Luu Duc Loc ; msv : 205751030110045")
print (" ############################# ")
#############################
def  benefit( t: float, n: float , k: int) -> float:
    p=n*(t/100)*k
    return p
n= float(input(" nhap so von ban dau: "))
t= float(input(" nhap % lai suat/thang: "))
k= int(input("nhap so thang gui: "))
print (" lai suat cuoi ky : {:,}".format(benefit(t,n,k)))
