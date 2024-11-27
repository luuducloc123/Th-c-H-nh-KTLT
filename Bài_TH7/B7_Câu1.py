print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
input_file =open('D:/a.txt','r')
for line in input_file:
    l=len(line)
    S=''
    while l>=1:
        s=S+line [l-1]
        l=l-1
    print(s)
input_file.close()
