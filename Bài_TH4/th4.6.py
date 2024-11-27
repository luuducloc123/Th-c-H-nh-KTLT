print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
def tach_ten_ho_dem():
   ho_ten_day_du = input("Nhập họ tên đầy đủ của bạn: ")

   # Tách họ và tên ra khỏi chuỗi nhập vào
   ho_dem, ten = ho_ten_day_du.split(' ', 1)

   print("Tên của bạn là:", ten)
   print("Họ đệm của bạn là:", ho_dem)

tach_ten_ho_dem()
