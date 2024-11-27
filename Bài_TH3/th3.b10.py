print ( " sv: Luu Duc Loc ; msv : 205751030110045")
print (" ############################# ")
#############################
import math
def tinh_chu_vi_dien_tich_hinh_tron(ban_kinh):
    chu_vi = 2 * math.pi * ban_kinh
    dien_tich = math.pi * (ban_kinh ** 2)
    return chu_vi, dien_tich
# Nhập bán kính từ người dùng
ban_kinh = float(input("Nhập bán kính của hình tròn: "))
chu_vi, dien_tich = tinh_chu_vi_dien_tich_hinh_tron(ban_kinh)
# In kết quả
print(f"Chu vi của hình tròn là: {chu_vi:.2f}")
print(f"Diện tích của hình tròn là: {dien_tich:.2f}")
