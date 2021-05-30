####################################################################################################
# Description:		Constant values used throughout simulation
# Author(s):		Joshua Geiser, Youssef Noureddine
# Last Modified:	05/2020

import numpy as np

class Constants():

	GRAVITY = 9.81; # Acceleration due to gravity
	GRAVITY_ENU = np.array([0, 0, GRAVITY]) # Acceleration vector due to gravity
	TOLERANCE = 1e-05; # Tolerance used in various sim calculations
	RHO_0 = 1.225; # Density of air at sea level
