print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
# Nhập chuỗi từ bàn phím
input_string = input("Nhập chuỗi: ")

# Loại bỏ tất cả các chữ số
output_string = ''.join( chuoi for chuoi in input_string if not chuoi.isdigit())

# In ra chuỗi mới
print("Chuỗi sau khi loại bỏ chữ số:", output_string)
