print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
# Nhập dãy các từ từ bàn phím
input_string = input("Nhập dãy các từ cách nhau bằng dấu cách: ")
# Tách các từ và lưu vào danh sách
words = input_string.split()
# Tìm độ dài lớn nhất của các từ
max_length = max(len(word) for word in words)
# Tìm tất cả các từ có độ dài lớn nhất
longest_words = [word for word in words if len(word) == max_length]
# In ra các từ dài nhất
print("Các từ dài nhất: ", ",".join(longest_words))
