#!/usr/bin/env python

####################################################################################################
# Description:        Executable input deck to vary inputs and run simulation
# Author(s):        Joshua Geiser, Youssef Noureddine
# Last Modified:    05/2020

import numpy as np

from aircraft import Aircraft
from atmosphere import Atmosphere, Wind
from constants import Constants
import sim_setup

from Planes.B737 import B737
from Planes.C172 import C172
from Planes.T38 import T38
from Planes.B17 import B17
from Planes.B747 import B747

# Initialization of objects used in overall sim architecture
SIM = sim_setup.Sim_Parameters()
CONSTANTS = Constants()
Atmosphere = Atmosphere()
plane1 = Aircraft()

####################################################################################################
# BEGIN INPUT FIELDS
####################################################################################################

# Modify simulation parameters
SIM.START_TIME = 0.0        #should always keep to 0
SIM.END_TIME = 20000.0
SIM.DELTA_T = 2             #time increments between each interval on plots in seconds

# Modify aircraft inital conditions 

# Choose airplane type - B737, C172, T38, B747, B17
plane1.design = B737()

# Input initial position vector (ex: [0, 0, 10000] to begin at 10000 m altitude)
plane1.state.pos_ENU = np.array([0, 0, 9000])
# Input initial velocity vector (ex: [260, 0, 0] for an initial velocity of 260 m/s eastward
plane1.state.vel_ENU = np.array([240, 0, 0])

# Input angle of attack (in radians)
plane1.aero.AoA = 0.08

# Mass of fuel at start of simulation in kg
FuelMass = 10000

####################################################################################################
# END INPUT FIELDS
####################################################################################################

# Command to begin running of simulation after input deck
sim_setup.Run_Sim(SIM, CONSTANTS, Atmosphere, plane1,FuelMass)

