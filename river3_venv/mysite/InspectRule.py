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

    RPI_point=(O2_point+BOD_point+SS_point+N2_point)/4
    return (RPI_point)

def Rule_O2(O2):
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

        return (O2_point)

def Rule_BOD(BOD):
        O2_point=0
        BOD_point=0
        SS_point=0
        N2_point=0
        if BOD<3:
           BOD_point=1
        if BOD>=3 and BOD<5:
           BOD_point=3
        if BOD>=5 and BOD<=15:
           BOD_point=6
        if BOD<15:
           BOD_point=10
        return BOD_point

def Rule_SS(SS):
        O2_point=0
        BOD_point=0
        SS_point=0
        N2_point=0
        if SS<20:
            SS_point=1
        if SS>=20 and SS<50:
            SS_point=3
        if SS>=50 and SS<=100:
            SS_point=6
        if SS>100:
            SS_point=10
        return SS_point


def Rule_N2(N2):
        O2_point=0
        BOD_point=0
        SS_point=0
        N2_point=0
        if N2<0.5:
            N2_point=1
        if N2>=0.5 and N2<1:
            N2_point=3
        if N2>=1 and N2<=3:
            N2_point=6
        if N2>3:
            N2_point=10
        return N2_point


def RPIInspect (point):
    point_Result=('DEFAULT_OUTPUT')
    if point<2:
        point_Result=('未(稍)受汙染')
    if point>=2 and point <=3:
        point_Result=('輕度汙染')
    if point>=3 and point<=6:
        point_Result=('中度汙染')
    if point>6:
        point_Result=('嚴重汙染')
    return point_Result

#====================WQI_Rule===========================

def WQI_PH(PH):
    PH_point=0
    if PH>=6.5 and PH<=8.5:
        PH_point=1
    else:
        PH_point=2
    return PH_point

def WQI_O2(O2):
    O2_point=0
    if O2=="ND":
        O2_point=6
    if O2>=6.5:
        O2_point=1
    if O2>=5.5:
        O2_point=2
    if O2>=4.5:
        O2_point=3
    if O2>=3:
        O2_point=4
    if O2<3:
        O2_point=5
    return O2_point

def WQI_BOD(BOD):
    BOD_point=0
    if BOD=="ND":
        BOD_point=1
    if BOD<=1:
        BOD_point=1
    if BOD<=2:
        BOD_point=2
    if BOD<=4:
        BOD_point=3
    if BOD>4:
        BOD_point=4
    return BOD_point

def WQI_SS(SS):
    SS_point=0
    if SS=="ND":
        SS_point=1
    if SS<=25:
        SS_point=1
    if SS<=40:
        SS_point=3
    if SS<=100:
        SS_point=4
    if SS>100:
        SS_point=5
    return SS_point

def WQI_CFU(CFU):
    CFU_point=0
    if CFU=="ND":
        CFU_point=1
    if CFU<=50:
        CFU_point=1
    if CFU<=5000:
        CFU_point=2
    if CFU<=10000:
        CFU_point=3
    if CFU>10000:
        CFU_point=4
    return CFU_point

def WQI_N2(N2):
    N2_point=0
    if N2=="ND":
        N2_point=1
    if N2<=0.1:
        N2_point=1
    if N2<=0.3:
        N2_point=2
    if N2>0.3:
        N2_point=4
    return N2_point

def WQI_TP(TP):
    TP_point=0
    if TP=="ND":
        TP_point=1
    if TP<=0.02:
        TP_point=1
    if TP<=0.05:
        TP_point=2
    if TP>0.05:
        TP_point=3
    return TP_point

def WQI_level(WQI_PH,WQI_O2,WQI_BOD,WQI_SS,WQI_CFU,WQI_N2,WQI_TP):
    maxpoint=max(WQI_PH,WQI_O2,WQI_BOD,WQI_SS,WQI_CFU,WQI_N2,WQI_TP)
    return maxpoint
