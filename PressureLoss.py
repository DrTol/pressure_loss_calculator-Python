# Pipe pressure loss calculator for a circular pipe, full flow water (SI Units) - Darcy-Weisbach
#   prepared by Hakan İbrahim Tol, PhD

def PressureLoss_DW(L,D,mFlow,T,aRou):
    # Inputs
    #   L       : Length of pipe segment        [m]
    #   D       : Pipe inner diameter           [mm]
    #   aRou    : Absolute roughness of pipe    [mm]
    #   mFlow   : Mass flow rate                [kg/s]
    #   T       : Water temperature             [ºC]

    # Output
    #   PL      : Pressure loss                 [bar]

    from DarcyFrictionFactor import f_Clamond
    from SubFunctions import Reynolds
    import XSteamPython as XSteam
    from math import pi

    # Reynolds number [-]
    Re=Reynolds(mFlow,D,T)

    # Darcy friction factor, f
    if Re<2300:
        f=64/Re
    else:
        f=f_Clamond(Re,aRou/D)

    PL=(8*f*L*mFlow**2/(pi**2*XSteam.rhoL_T(T)**2*9.81*(D/1000)**5))/10.1971621297792

    return PL
    
    
