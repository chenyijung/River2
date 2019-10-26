import math


def RPI(O2,BOD,SS,N2):
    O2_point=0
    BOD_point=0
    SS_point=0
    N2_point=0
    
    if O2>6.5:
        O2_point=1
    if O2<=6.5 and O2>4.5:
        O2_point=3
    if O2<=4.5 and O2>=2.0:
        O2_point=6
    if O2<2.0:
        O2_point=10


    if BOD<3:
       BOD_point=1
    if BOD>=3 and BOD<5:
       BOD_point=3
    if BOD>=5 and BOD<=15:
       BOD_point=6
    if BOD<15:
       BOD_point=10


    if SS<20:
        SS_point=1
    if SS>=20 and SS<50:
        SS_point=3
    if SS>=50 and SS<=100:
        SS_point=6
    if SS>100:
        SS_point=10

    if N2<0.5:
        N2_point=1
    if N2>=0.5 and N2<1:
        N2_point=3
    if N2>=1 and N2<=3:
        N2_point=6
    if N2>3:
        N2_point=10

    RPI_point=O2_point+BOD_point+SS_point+N2_point
    return (RPI_point)



def RPIInspect (point):
    point_Result=('DEFAULT_OUTPUT')
    if point<2:
        point_Result=('None')
    if point>=2 and point <=3:
        point_Result=('LOW')
    if point>=3 and point<=6:
        point_Result=('MEDIUM')
    if point>6:
        point_Result=('HIGH')
    return point_Result
