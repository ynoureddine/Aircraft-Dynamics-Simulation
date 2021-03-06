####################################################################################################
# Description:        Design geometry for a Cessna 172 aircraft
#
# Cruise Velocity:    55 m/s
# Cruise Altitude:     3000 m
#
# Author(s):        Joshua Geiser
# Last Modified:    12/2018

import numpy as np

class C172():

    name = "C172"

    mass = 1000 # kg
    mass_matrix = np.identity(3) * mass

    wingarea = 16.00 # m^2
    wingspan = 11.00 # m
    chord = 1.454545 # m

    max_thrust = 1500 # N

    CDi = 0.027 # CD due to induced drag
    
    max_velocity = 84.0435    # Top speed of the aircraft in m/s
    max_fuel_consumption = 0.00756 # Max fuel consumption of the aircraft in kg/s
    max_fuel_mass = 117            # The maximum fuel the fuel tanks can store in kg
    empty_mass = 883               # The dry mass of the aircraft in kg
