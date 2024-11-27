print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
         for line in islice(f, nlines):
             print(line)
file_read_from_head('D:/test.txt',2)
