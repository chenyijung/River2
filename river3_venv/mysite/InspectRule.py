import math
O2_point=0

def RPI(O2,bioo2,solid,N2):
    if O2>6.5:
        O2_point=1
    if O2<=6.5 and O2>=4.6:
        O2_point=3
    if O2<=4.5 and O2>=2.0:
        O2_point=6
    if O2<2.0:
        O2_point=10
    return O2_point
