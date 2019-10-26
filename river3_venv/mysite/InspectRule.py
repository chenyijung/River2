import math
O2_point=0
bioo2_point=0
solid_point=0
N2_point=0

def RPI(O2,bioo2,solid,N2):
    if O2>6.5:
        O2_point=1
    if O2<=6.5 and O2>4.5:
        O2_point=3
    if O2<=4.5 and O2>=2.0:
        O2_point=6
    if O2<2.0:
        O2_point=10


    if bioo2<3:
       bioo2_point=1
    if bioo2>=3 and bioo2<5:
       bioo2_point=3
    if bioo2>=5 and bioo2<=15:
       bioo2_point=6
    if bioo2<15:
       bioo2_point=10


    if solid<20:
        solid_point=1
    if solid>=20 and solid<50:
        solid_point=3
    if solid>=50 and solid<=100:
        solid_point=6
    if solid>100:
        solid_point=10


    if N2<0.5:
        N2_point=1
    if N2>=0.5 and N2<1:
        N2_point=3
    if N2>=1 and N2<=3:
        N2_point=6
    if N2>3:
        N2_point=10

    RPI_point=O2_point+bioo2_point+solid_point+N2_point
    return (RPI_point,O2_point,bioo2_point,solid_point,N2_point)
