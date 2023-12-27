# Pipe pressure loss calculator for a circular pipe, full flow water (SI Units) - Darcy-Weisbach
#   prepared by Hakan İbrahim Tol, PhD

from DarcyFrictionFactor import f_Clamond
from SubFunctions import *
from CoolProp.CoolProp import PropsSI
from math import pi

def PressureLoss_DW(L,D,mFlow,T,aRou,P,fluid_name):
    # Inputs
    #   L       : Length of pipe segment        [m]
    #   D       : Pipe inner diameter           [mm]
    #   aRou    : Absolute roughness of pipe    [mm]
    #   mFlow   : Mass flow rate                [kg/s]
    #   T       : Fluid temperature             [ºC]
    #   P       : Fluid pressure                [bar]
    #   fluid_name   : Fluid name

    # Output
    #   PL      : Pressure loss                 [bar]

    # Reynolds number [-]
    Re=Reynolds(mFlow,D,T,P,fluid_name)

    # Darcy friction factor, f
    if Re<2300:
        f=64/Re
    else:
        f=f_Clamond(Re,aRou/D)
        
    rho=PropsSI('D', 'T', T+273.15, 'P', P*1e5, fluid_name)

    PL=(8*f*L*mFlow**2/(pi**2*rho**2*9.81*(D/1000)**5))/10.1971621297792

    return PL  
