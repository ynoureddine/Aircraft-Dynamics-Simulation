# Aircraft-Dynamics-Simulation

This project was done as part of a research project under Prof. Dengfeng Sun at Purdue University during Spring 2020.

# Project Features

We use a set of input arguments to predict multiple aspects of the trajectory of the aircraft.

Given:
- Plane Model: choose from B737, C172, T38, B747, B17
- Initial mass of fuel.
- Initial position.
- Initial velocity.
- Angle of Attack

We are able to predict:
- Cruising Velocity
- Cruising Altitude
- Fuel consumption rate
- General aircraft trajectory
- Resultant forces

To run the code, run the executable "inputs.py" file here is where you should also make any changes to the initial conditions of the flight. After a run, you will either receive a message stating that the simulation has been sucesffuly calculated or that the aircraft has crashed or ran out of fuel, whichever comes first. In all cases, an output.csv file in the post processing folder is created with flight parameters throughout the simulation. A script in the same folder called "plot.py" can then be run that will produce the appropriate plots for the flight simulation.

