from math import pi
from CoolProp.CoolProp import PropsSI

def Reynolds(mFlow,D,T,P,fluid_name):
# Calculates the Reynolds Number for a circular pipe (water)

# INPUTS (scalar or vector)
#   MF  : Mass flow                     [kg/s]
#   D   : Inner diameter of the pipe	[mm]
#   T   : Temperature of the water      [°C]
#   P       : Fluid pressure            [bar]
#   fluid_name   : Fluid name
    
    V = PropsSI('V', 'T', T+273.15, 'P', P*1e5, fluid_name)

    Reynolds = 4*mFlow/(pi*(D/1000)*V)

    return Reynolds
