####################################################################################################
# Description:        Design geometry for a T-38 aircraft
#    
# Cruise Velocity:    156 m/s
# Cruise Altitude:     16700 m
#
# Author(s):        Joshua Geiser
# Last Modified:    12/2018

import numpy as np

class T38():

    name = "T38"

    mass = 5360 # kg
    mass_matrix = np.identity(3) * mass

    wingarea = 15.79 # m^2
    wingspan = 7.600 # m
    chord = 2.077632 # m

    max_thrust = 25800 # N

    CDi = 0.10 # CD due to induced drag
    
    max_velocity = 383.56           # Top speed of the aircraft in m/s
    max_fuel_consumption = 1.44     # Max fuel consumption of the aircraft in kg/s
    fuel_mass = 2094                # The maximum fuel the fuel tanks can store in kg
    empty_mass = 3266               # The dry mass of the aircraft in kg

