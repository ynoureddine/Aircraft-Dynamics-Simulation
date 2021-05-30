####################################################################################################
# Description:        Design geometry for a B-17 aircraft
#    
# Cruise Velocity:    81.4 m/s
# Cruise Altitude:     3000 m
#
# Author(s):        Alan Gelman
# Last Modified:    04/2020

import numpy as np

class B17():

    name = "B17"

    mass = 24500 # kg
    mass_matrix = np.identity(3) * mass

    wingarea = 132.92 # m^2
    wingspan = 103.75 # m
    chord = 4.17 # m

    max_thrust = 50000 # N

    CDi = 0.039 # CD due to induced drag
    
    max_velocity = 128.3             # Top speed of the aircraft in m/s
    max_fuel_consumption = 0.246     # Max fuel consumption of the aircraft in kg/s
    max_fuel_mass = 5167             # The maximum fuel the fuel tanks can store in kg
    empty_mass = 16391               # The dry mass of the aircraft in kg

