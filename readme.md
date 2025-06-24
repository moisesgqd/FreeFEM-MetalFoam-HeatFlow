# About the properties data file

The numbers in the thermophysical parameters file represent physical quantities in the international metric system.

They represent:
- g: gravity constant in m/s^2
- sgm: Stefan-Boltzmann constant in W/(m^2-K^4)
- eC: emissivity of glass cover, no dimensional
- eP: emissivity of collector plate, no dimensional
- rhof: fluid density in kg/m^3
- cpf: fluid specific heat in J/(kg-K)
- mu: fluid dynamic viscosity in Pa/s or N-s/m^2
- kf: fluid phase thermal conductivity in W/(m-K)
- rhos: solid density in kg/m^3
- cps: solid specific heat in J/(kg-K)
- ks: solid thermal conductivity in W/(m-K)

 Although order could be altered, consider **only modifying the numerical values** of the properties.

Based on the values, the program calculates the kinematic viscosity, thermal diffusivities for the fluid and the solid phases, and Prandtl number.
