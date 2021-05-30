####################################################################################################
# Description:        Design geometry for a Boeing 747 aircraft
#    
# Cruise Velocity:    257 m/s
# Cruise Altitude:     10700 m
#
# Author(s):        Alan Gelman
# Last Modified:    04/2020

import numpy as np

class B747():

    name = "B747"

    mass = 375000 # kg
    mass_matrix = np.identity(3) * mass

    wingarea = 524.7 # m^2
    wingspan = 54.5 # m
    chord = 8.32 # m

    max_thrust = 1126000 # N

    CDi = 0.042 # CD due to induced drag
    
    max_velocity = 301                # Top speed of the aircraft in m/s
    max_fuel_consumption = 2.384      # Max fuel consumption of the aircraft in kg/s
    max_fuel_mass = 194000            # The maximum fuel the fuel tanks can store in kg
    empty_mass = 181000               # The dry mass of the aircraft in kg
    

