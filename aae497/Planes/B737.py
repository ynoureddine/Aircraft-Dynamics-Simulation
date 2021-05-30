####################################################################################################
# Description:        Design geometry for a Boeing 737 aircraft
#    
# Cruise Velocity:    230 m/s
# Cruise Altitude:     9145 m
#
# Author(s):        Joshua Geiser
# Last Modified:    12/2018

import numpy as np

class B737():

    name = "B737"

    mass = 50000 # kg
    mass_matrix = np.identity(3) * mass

    wingarea = 124.6 # m^2
    wingspan = 34.32 # m
    chord = 3.630536 # m

    max_thrust = 242800 # N

    CDi = 0.043 # CD due to induced drag
    
    max_velocity = 263               # Top speed of the aircraft in m/s
    max_fuel_consumption = 0.703     # Max fuel consumption of the aircraft in kg/s
    max_fuel_mass = 20920            # The maximum fuel the fuel tanks can store in kg
    empty_mass = 41000               # The dry mass of the aircraft in kg
