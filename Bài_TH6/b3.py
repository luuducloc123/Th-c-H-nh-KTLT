print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
class Nguoi(object):
    def getGender( self ):
     return "Unknown"
class Nam( Nguoi ):
    def getGender( self ):
     return "Nam"
class Nu( Nguoi ):
    def getGender( self ):
     return "Nữ"
aNam = Nam()
aNu= Nu()
print (aNam.getGender())
print (aNu.getGender())
