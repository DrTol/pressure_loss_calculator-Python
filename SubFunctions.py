def Reynolds(mFlow,D,T):
# Calculates the Reynolds Number for a circular pipe (water)

# INPUTS (scalar or vector)
#   MF  : Mass flow                     [kg/s]
#   D   : Inner diameter of the pipe	[mm]
#   T   : Temperature of the water      [°C]

    P=8*100     # [kPa] Pressure

    from math import pi
    from XSteamPython import my_pT

    Reynolds = 4*mFlow/(pi*(D/1000)*my_pT(P,T))

    return Reynolds
