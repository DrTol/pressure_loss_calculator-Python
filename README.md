# Pressure Loss Calculator Tool - Python (SI Units)
A Python tool calculating the friction pressure loss (head loss) in circular pipes with full flow water, based on Darcy-Weisbach using Clamond algorithm for the friction factor. 

- Excel functions (also as add-in) for the same calculator/s can be found in [pressure_loss_calculator-Excel.git](https://github.com/DrTol/pressure_loss_calculator-Excel.git).
- Matlab functions for the same calculator/s can be found in [pressure_loss_calculator-Matlab.git](https://github.com/DrTol/pressure_loss_calculator-Matlab).

## Requirements
This tool requires that `XSteamPython` and `SciPy` be installed. Please see [XSteamPython.git](https://github.com/raldridge11/XSteamPython)

## How2Use
Please see [ExampleScript.py](https://github.com/DrTol/pressure_loss_calculator-Python/blob/master/ExampleScript.py)

## License
You are free to use, modify and distribute the code as long as authorship is properly acknowledged. The same applies for the original works 'XSteam.m' by Holmgren M. and 'colebrook.m' by Clamond D, this repository Python tools make use of.

## Acknowledgement 
In memory of my mother Esma Tol and my father Bekir Tol.

We would like to acknowledge all of the open-source minds in general for their willing of share (as apps or comments/answers in forums), which has encouraged our department to publish our Python tools developed during the PhD study here in GitHub.

## How2Cite:
1. Tol, Hİ. pressure_loss_calculator-Python. DOI: 10.5281/zenodo.3268807. GitHub Repository 2018; https://github.com/DrTol/pressure_loss_calculator-Python
2. Tol, Hİ. District heating in areas with low energy houses - Detailed analysis of district heating systems based on low temperature operation and use of renewable energy. PhD Supervisors: Svendsen S. & Nielsen SB. Technical University of Denmark 2015; 204 p. ISBN: 9788778773685.

## References
- Sanks RL. Flow in conduits. In: Sanks RL, Tchobanoglous G, Bosserman BE, Jones GM, editors. Pumping station design. Boston, USA: Butterworth-Heinemann 1998: p. 33-39.
- Clamond D. Efficient resolution of the colebrook equation. Industrial & Engineering Chemistry Research 2009; 48: p. 3665-3671.
- Clamond D. colebrook.m - Efficient resolution of the Colebrook-White equation (v1.0). MathWorks File Exchange: https://nl.mathworks.com/matlabcentral/fileexchange/21990-colebrook-m?focused=5105324&tab=function
- Colebrook CF & White CM. Experiments with fluid friction in roughened pipes. Proceedings of the Royal Society A - Mathematical, Physical & Engineering Sciences 1937: p. 367-381.
- Asker M, Turgut OE & Coban MT. A review of non iterative friction factor correlations for the calculation of pressure drop in pipes. Bitlis Eren Univ J Sci & Technol 2014; 4(1): 8 p. 
- Genić S, Arandjelović I, Kolendić P, Jarić M, Budimir N & Genić M. A Review of explicit approximations of Colebrook’s equation. FME Transactions 2011; 39: p. 67-71. 
- Holmgren M. X Steam, Thermodynamic properties of water and steam (v1.0). MathWorks File Exchange: https://nl.mathworks.com/matlabcentral/fileexchange/9817-x-steam--thermodynamic-properties-of-water-and-steam
