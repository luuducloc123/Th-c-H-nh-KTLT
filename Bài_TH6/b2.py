print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
class Hinhchunhat(object):
    def __init__ (self, a,b):
        self.dai = a
        self.rong = b
###########################
    def area (self):
        return self.dai*self.rong
a= int(input("Nhập chiều dai: "))
b = int (input("Nhập chiều rộng: "))
aHinhchunhat = Hinhchunhat(a,b)
print ("Diện tích là: ",aHinhchunhat.area())
