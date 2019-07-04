## returns the Darcy-Weisbach friction factor for pressure loss calculations
#   prepared by Hakan İbrahim Tol, PhD on 02/07/2019

import math
import warnings

# via Clamond algorithm _ Copied,Modified,Pasted! 
def f_Clamond(R,K=0):
# DWc = COLEBROOK(R,K) fast, accurate and robust computation of the 
#     Darcy-Weisbach friction factor F according to the Colebrook equation:
#                             -                       -
#      1                     |    K        2.51        |
#  ---------  =  -2 * Log_10 |  ----- + -------------  |
#   sqrt(DWc)                |   3.7     R * sqrt(DWc) |
#                             -                       -
# INPUT:
#   R : Reynolds' number (should be >= 2300).
#   K : Equivalent sand roughness height divided by the hydraulic 
#       diameter (default K=0).
#
# OUTPUT:
#   DWc : Darcy Weisbach Friction factor.
#
# FORMAT:
#   R, K and DWc are ONLY scalars in this Python Module
#
# ACCURACY:
#   Around machine precision forall R > 3 and forall 0 <= K, 
#   i.e. forall values of physical interest. 
#
# EXAMPLE: DWc = f_Clamond(7e5,0.01)
#
# Method: Quartic iterations.
# Reference: http://arxiv.org/abs/0810.5564 
# Read this reference to understand the method and to modify the code.

# Author: D. Clamond, 2008-09-16.
# Modified for Python by Hakan İbrahim Tol, PhD, 2019-07-02

    # Check for errors.
    if R<2300:
       warnings.warn('The Colebrook equation is valid for Reynolds'' numbers >= 2300.')      

    if K<0: 
       warnings.warn('The relative sand roughness must be non-negative.') 

    # Initialization.
    X1 = K * R * 0.123968186335417556               # X1 <- K * R * log(10) / 18.574.
    X2 = math.log(R) - 0.779397488455682028         # X2 <- log( R * log(10) / 5.02                    

    # Initial guess.                                              
    DWc = X2 - 0.2     

    # First iteration.
    E = ( math.log(X1+DWc) - 0.2 ) / ( 1 + X1 + DWc )
    DWc = DWc - (1+X1+DWc+0.5*E) * E *(X1+DWc) / (1+X1+DWc+E*(1+E/3))

    # Second iteration (remove the next two lines for moderate accuracy).
    E = ( math.log(X1+DWc) + DWc - X2 ) / ( 1 + X1 + DWc )
    DWc = DWc - (1+X1+DWc+0.5*E) * E *(X1+DWc) / (1+X1+DWc+E*(1+E/3))

    # Finalized solution.
    DWc = 1.151292546497022842 / DWc                # DWc <- 0.5 * log(10) / DWc;
    DWc = DWc * DWc                                 # DWc <- Friction factor.

    return DWc

# via solving implicit Colebrook-White equation
def f_ColebrookWhite(D,Re,aRou,fTol=0.001,MaxIter=2000):

    #   INPUTS
    #   D       : Inner diameter of the pipe          [mm]
    #   Re      : Reynolds Number                     [-]
    #   aRou    : Absolute roughness of pipe          [mm]
    #   fTol    : Iteration termination tolerance
    #   MaxIter : Maximum limit (iteration)

    # Initializing the Iteration
    error=10;                   # Iteration error 
    IterNum=0;                  # Iteration steps number
    x0=f_SwameeJain(D,Re,aRou)  # Initial estimate

    # Fasten your seat belts - Iteration starts
    while error>fTol and IterNum<MaxIter:
        x1 = (2*math.log10((aRou/D)/3.7+2.51/(Re*math.sqrt(x0))))**(-2)
        error=abs(x1-x0)
        IterNum=IterNum+1
        x0=x1

    return x1

# via solving explicit equation by Swamee PK & Jain AK
def f_SwameeJain(D,Re,aRou):

    #   INPUTS
    #   D       : Inner diameter of the pipe          [mm]
    #   Re      : Reynolds Number                     [-]
    #   aRou    : Absolute roughness of pipe          [mm]

    # Checking limitations
    if Re<5000 or Re>1e8:
        warnings.warn('Swamee&Jain algorithm is valid for a Reynold range as in 5000<Re<1e8')

    if aRou/D<1e-6 or aRou/D>0.05:
        warnings.warn('Swamee&Jain algorithm is valid for a relative roughness range as in 1e-6<eps/D<0.05')

    # Calculation

    f=0.25/(math.log10((aRou/D)/3.7+5.74/Re**0.9))**2

    return f
