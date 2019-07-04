# Pipe pressure loss - Circular pipe, full flow water in SI Units
# based on Darcy-Weisbach, using Clamond algorithm for friction factor

# Inputs
D=70.3      # [mm]      Pipe diameter
aRou=0.1    # [mm]      Absolute roughness
mFlow=4.09  # [kg/s]    Mass flow rate
T=90        # [ºC]      Water temperature
L=66        # [m]       Pipe length

## Main Function that returns the pressure loss
import PressureLoss as PL

print("Pressure Loss [bar] = ", PL.PressureLoss_DW(L,D,mFlow,T,aRou))

## Other Functions

# Function that returns Reynolds number
import SubFunctions as SF
Re=SF.Reynolds(mFlow,D,T)
print("Reynolds = ", Re)

# Functions that return Darcy Friction Factor, f
import DarcyFrictionFactor as DF

print("Darcy Friction Factor via ColebrookWhite = ", DF.f_ColebrookWhite(D,Re,aRou))
print("Darcy Friction Factor via SwameeJain = ", DF.f_SwameeJain(D,Re,aRou))
print("Darcy Friction Factor via Clamond = ", DF.f_Clamond(Re,aRou/D))
